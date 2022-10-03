#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from turtlesim_helper.msg import UnitsLabelled
import math


class homework3:
    def __init__(self):
        self.total = 0
        self.Xold = 0
        self.Yold = 0
        self.pub_msg = UnitsLabelled()
        self.pub_msg.units = "meters"
        rospy.Subscriber("turtle1/pose", Pose, self.callback)
        self.pub_units = rospy.Publisher("turtle1/cmd_vel", UnitsLabelled, queue_size=10)

        

    def callback(self,msg):
        self.Xnew = 0
        self.Ynew = 0
        self.total += math.sqrt(pow((self.Xnew-self.Xold),2)+pow((self.Ynew-self.Yold),2))
        self.pub_msg.value = self.total
        self.pub_units.publish(self.pub_msg)



if __name__=='__main__':
    rospy.init_node('check_sub')
    homework3()
    rospy.spin()

