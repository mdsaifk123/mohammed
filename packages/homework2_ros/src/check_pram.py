#!/usr/bin/env python3

import rospy
from turtlesim_helper.msg import UnitsLabelled


class check_pram:
    def __init__(self):
        if rospy.has_pram("converter"):
            self.foo = rospy.get_pram("converter")
        else:
            self.foo = "default"

        self.msg = UnitsLabelled()
        self.msg.units = "smoots"
        rospy.Subscriber("output1", UnitsLabelled, self.callback)
        self.units = rospy.Publisher("output2", UnitsLabelled, queue_size=10)
        self.units.publish(self.msg)


    def callback(self,msg):
        
        #funtion  for conversion
        meters = 0.3048*(msg.msg)
        smoots = (msg.msg)/5.583
        feet = msg.msg

        if (param == "smoots"):
            msg.units = smoots
            self.units.publish(self.msg)

        elif (param == "meters"):
            msg.units = meters
            self.units.publish(self.msg)

        elif (param == "feet"):
            msg.units = feet
            self.units.publish(self.msg)


if __name__=='__main__':
    rospy.init_node('check_pram')
    check_pram()
    rospy.spin()