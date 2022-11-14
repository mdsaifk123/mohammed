#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32, String
from pid import PID

class homework9:
    def __init__(self):
        #publishes to the control_input  
        self.pub = rospy.Publisher("/control_input", Float32, queue_size=10)
        self.get_pid = PID(p=0.08, i=0.025, d=0.5)
        
        #set the parameter controller_ready to true
        rospy.set_param("controller_ready", "true") 
        
        #subscribes messages error topics published above
        rospy.Subscriber("/error", Float32, self.callback)



    # call PID class' control calculation when receiving error message
    def callback(self, error):
        #pid values changed using the received error
        result = self.get_pid.feedback_control(error.data, 0.009)
        
        #new controller message 
        self.pub.publish(result)



if __name__ == '__main__':

    rospy.init_node('homework9')
    rospy.sleep(5)
    homework9()
    rospy.spin()