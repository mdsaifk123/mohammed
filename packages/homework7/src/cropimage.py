#!/usr/bin/env python3

import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Homework7:
    def __init__(self):
        self.bridge = CvBridge()
        rospy.Subscriber("/image", Image, self.callback)
        #publishers
        #image_cropped topic
        self.pub_crop = rospy.Publisher("/image_cropped", Image, queue_size=10)
        #image_white topic
        self.pub_white = rospy.Publisher("/image_white", Image, queue_size=10)
        #image_yellow topic
        self.pub_yellow = rospy.Publisher("/image_yellow", Image, queue_size=10)

    
    def callback(self, msg):
        #convert to a ROS image using bridge
        cv_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        
        #crops image 
        cv_cropped = cv_img[int(cv_img.shape[0]/2):cv_img.shape[0], 0:cv_img.shape[1]]

        #convert and filter from BGR to HSV
        hsv_img = cv2.cvtColor(cv_cropped, cv2.COLOR_BGR2HSV)
        
        #convert new image to ROS 
        ros_cropped = self.bridge.cv2_to_imgmsg(cv_cropped, "bgr8")

        
        #the cropped image
        self.pub_crop.publish(ros_cropped)

        #filter white lane
        white_filter = cv2.inRange(hsv_img, (0,0,225),(180,40,255))

        ros_white = self.bridge.cv2_to_imgmsg(white_filter, "mono8")

        #white filtered image
        self.pub_white.publish(ros_white) 

        #filter yellow lane
        yellow_filter = cv2.inRange(hsv_img, (0,150,180),(70,255,255))

        ros_yellow = self.bridge.cv2_to_imgmsg(yellow_filter, "mono8") 
 
        #yellow filtered image
        self.pub_yellow.publish(ros_yellow)     

if __name__=="__main__":
    # initialize publisher node
    rospy.init_node("homework7")
    Homework7()
    rospy.spin()
