#!/usr/bin/env python3

from tkinter import UNITS
import rospy
from turtlesim_helper.msg import UnitsLabelled



class check_param:
    def __init__(self):

        rospy.Subscriber("output1", UnitsLabelled, self.callback)
        self.msg = UnitsLabelled()
        self.msg.units = self.unit
        self.units = rospy.Publisher("output2", UnitsLabelled, queue_size=10)
      


    def callback(self,msg):
    
        if rospy.has_param("/converter"):
            self.unit = rospy.get_param("/converter")
        else:
            self.unit = "default"


        if (self.unit == "meters"):
            self.msg.value = msg.value
            self.units.publish(self.msg)

        elif (self.unit == "feet"):
            self.msg.value = msg.value*3.28084
            self.units.publish(self.msg)

        else: 
            self.msg.value = msg.value*0.587613
            self.units.publish(self.msg)
        
        


if __name__=='__main__':
    rospy.init_node('check_param')
    check_param()
    rospy.spin()