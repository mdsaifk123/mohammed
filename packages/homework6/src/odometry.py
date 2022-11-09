#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32, String
from odometry_hw.msg import Pose2D, DistWheel #imported from ROS package
import math #for mathematical formulas

class Odom:
	def __init__(self):
	#Publisher with topic and message
		self.x = 0
		self.y = 0
		self.theta = 0
		self.pub = rospy.Publisher("/pose", Pose2D, queue_size=10)
		self.my2DPose = Pose2D(0,0,0) #Pose2D set to 0
		#Subscriber to distwheel topic
		rospy.Subscriber("/dist_wheel",DistWheel, self.callback)	

	#Calculating odemetry with rosbag values	
	def callback(self, disWheel):
		d_s = (disWheel.dist_wheel_left + disWheel.dist_wheel_right)/2
		d_theta = (disWheel.dist_wheel_right-disWheel.dist_wheel_left)/0.1
		d_x = d_s*math.cos(self.my2DPose.theta + d_theta/2)
		d_y = d_s*math.sin(self.my2DPose.theta + d_theta/2)
		self.my2DPose.x += d_x
		self.my2DPose.y += d_y
		self.my2DPose.theta += d_theta
		#creates the graph
		self.pub.publish(self.my2DPose)


if __name__ == '__main__':
	rospy.init_node('odometry')
	Odom()
	rospy.spin()
