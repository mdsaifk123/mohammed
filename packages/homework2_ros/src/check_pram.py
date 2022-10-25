#!/usr/bin/env python3

import rospy
from turtlesim_helper.msg import UnitsLabelled



class check_pram:
    def __init__(self):

        rospy.Subscriber("output1", UnitsLabelled, self.callback)
        self.units = rospy.Publisher("output2", UnitsLabelled, queue_size=10)
      


    def callback(self,msg):
    
        if rospy.has_param("converter"):
            self.foo = rospy.get_param("converter")
        else:
            self.foo = "default"

        #funtion  for conversion
        meters = (msg.msg)
        smoots = (msg.msg)/5.583
        feet = 0.3048*(msg.msg)

        if (param == "smoots"):
            msg.units = smoots

        else: 
            self.msg.value = msg.value*0.587613
            self.units.publish(self.msg)
        
        


if __name__=='__main__':
    rospy.init_node('check_pram')
    check_pram()
    rospy.spin()