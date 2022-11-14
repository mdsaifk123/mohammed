#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32, String

class PID:
    def __init__(self, p, i, d):
        #initializing gains
        self.kp = p
        self.ki = i
        self.kd = d
        self.prev_err = 0
        self.i = 0


 #controller design
    def feedback_control(self, error, dt):
        #update PID using the error value
        p = error
        self.i += (error * dt)
        d = (error - self.prev_err) / dt
        self.prev_err = error
        #returns calculated result
        pid_controller = (self.kp*p) + (self.ki * self.i) + (self.kd * d)
        return pid_controller
