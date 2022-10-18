#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
#from std_msgs.msg import Float32
from turtlesim_helper.msg import UnitsLabelled
import math


class check_sub:
    def __init__(self):
        self.total = 0
        self.Xold = 0
        self.Yold = 0
        self.pub_msg = UnitsLabelled()
        self.pub_msg.units = "meters"
        rospy.Subscriber("/turtle1/pose", Pose, self.callback)
        #self.pub_raw=rospy.Publisher("output1",Float32, queue_size=10)
        self.pub_units = rospy.Publisher("output1", UnitsLabelled, queue_size=10)
        self.pub_units.publish(self.pub_msg)
        

    def callback(self,msg):

        self.total += math.sqrt(pow(msg.x-self.Xold,2)+pow(msg.y-self.Yold,2))
        self.Xold = msg.x
        self.Yold = msg.y
        self.pub_msg.value = self.total
        #self.pub_raw.publish(self.total)
        self.pub_units.publish(self.pub_msg)



if __name__=='__main__':
    rospy.init_node('check_sub')
    check_sub()
    rospy.spin()

