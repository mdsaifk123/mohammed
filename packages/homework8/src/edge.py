#!/usr/bin/env python3


import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import message_filters
import numpy as np


class Homework8:
    def __init__(self):
        self.bridge = CvBridge()
        # subscribers
        self.sub_cropped = message_filters.Subscriber("image_cropped", Image)
        # subscribes to yellow topic
        self.sub_yellow = message_filters.Subscriber("image_yellow", Image)
        # subscribes to white topic
        self.sub_white = message_filters.Subscriber("image_white", Image)
	
	# time synchronizer
        self.ts = message_filters.TimeSynchronizer([self.sub_cropped, self.sub_yellow, self.sub_white], 10)
        self.ts.registerCallback(self.callback)


        self.pub_canny = rospy.Publisher("/image_edges",Image, queue_size=10)
        # publishes final white filtered image
        self.pub_white = rospy.Publisher("image_lines_white",Image, queue_size=10)
        # publishes final yellow filtered image
        self.pub_yellow = rospy.Publisher("image_lines_yellow",Image, queue_size=10)


    def callback(self, cropped_msg, yellow_msg, white_msg, ):

        # images to be edge detected
        cropped_cv = self.bridge.imgmsg_to_cv2(cropped_msg, "bgr8")
        yellow_cv = self.bridge.imgmsg_to_cv2(yellow_msg, "mono8")
        white_cv = self.bridge.imgmsg_to_cv2(white_msg, "mono8")
        

        # perform edge detection
        edges = cv2.Canny(cropped_cv,0,255)

         # convert canny image back to be published
        canny = self.bridge.cv2_to_imgmsg(edges, "mono8")
        self.pub_canny.publish(canny)


        # dilate function
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))

        # dilate filtered edges
        kernel_for_edges = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1))
        
        # dilate white/yellow images
        dilated_white = cv2.dilate(white_cv, kernel)
        dilated_yellow = cv2.dilate(yellow_cv, kernel)

        # dilate the edges
        dilated_edges = cv2.dilate(edges, kernel_for_edges)

        #  bitwise on white and yellow lines
        and_white = cv2.bitwise_and(dilated_edges, dilated_white, mask=None)
        and_yellow = cv2.bitwise_and(dilated_edges, dilated_yellow, mask=None)

        # white lines Probabilistic Hough Transform
        lines_white = cv2.HoughLinesP(and_white, 1, np.pi/180, 5, None, 10, 5)

        # yellow lines Probabilistic Hough Transform
        lines_yellow = cv2.HoughLinesP(and_yellow, 1, np.pi/180, 5, None, 2, 2)

        # draw blue line on the two images
        image_lines_white = self.output_lines(cropped_cv, lines_white)
        image_lines_yellow = self.output_lines(cropped_cv, lines_yellow)



        # convert images back to be published
        ros_white = self.bridge.cv2_to_imgmsg(image_lines_white, "bgr8")
        ros_yellow = self.bridge.cv2_to_imgmsg(image_lines_yellow, "bgr8")
       

        # publish white/yellow filtered images
        self.pub_white.publish(ros_white)
        self.pub_yellow.publish(ros_yellow)


    # draw blue lines 
    def output_lines(self, original_image, lines):
        output = np.copy(original_image)
        if lines is not None:
            for i in range(len(lines)):
                l = lines[i][0]
                cv2.line(output, (l[0],l[1]), (l[2],l[3]), (255,0,0), 2, cv2.LINE_AA)
                cv2.circle(output, (l[0],l[1]), 2, (0,255,0))
                cv2.circle(output, (l[2],l[3]), 2, (0,0,255))
        return output 

if __name__=="__main__":
    rospy.init_node("homework8")
    Homework8()
    rospy.spin()
