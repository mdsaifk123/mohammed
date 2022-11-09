#!/usr/bin/env python3

import rospy
import numpy as np
from duckietown_msgs.msg import Vector2D


class transform:

    def __init__(self):

        
        
        rospy.Subscriber("/sensor_coord", Vector2D, self.callback)
        self.pub_robot = rospy.Publisher("/robot_coord", Vector2D, queue_size = 10)
        self.pub_world = rospy.Publisher("/world_coord", Vector2D, queue_size = 10)
        self.pub_msg = Vector2D()

        robotx = 5
        roboty = 3
        sensorx = -1
        sensory = 0
        robotangle = 135
        sensorangle = 315 
        rRs = np.array([[np.cos(sensorangle*np.pi/180), -1*np.sin(sensorangle*np.pi/180)],[np.sin(sensorangle*np.pi/180), 1*np.cos(sensorangle*np.pi/180)]])
        rPs = np.array([[sensorx],[sensory]])
        row_L = np.array([0,0,1])
        rTs = np.concatenate((rRs, rPs), axis=1)

        self.rTs = np.vstack([rTs, row_L])
        wRr = np.array([[np.cos(robotangle*np.pi/180), -1*np.sin(robotangle*np.pi/180)],[np.sin(robotangle*np.pi/180), 1*np.cos(robotangle*np.pi/180)]])
        wPr = np.array([[robotx],[roboty]])
        wTr = np.concatenate((wRr, wPr), axis=1)
        self.wTr = np.vstack([wTr, row_L])


    def callback(self, msg):
        obstracle_sensor = np.array([[msg.x],[msg.y],[1]])
        obstracle_robot = np.matmul(self.rTs, obstracle_sensor)
        self.pub_msg.x = obstracle_robot.item((0,0))
        self.pub_msg.y = obstracle_robot.item((1,0))
        self.pub_robot.publish(self.pub_msg)
        obstracle_world = np.matmul(self.wTr, obstracle_robot)
        self.pub_msg.x = obstracle_world.item((0,0))
        self.pub_msg.y = obstracle_world.item((1,0))
        self.pub_world.publish(self.pub_msg)


if __name__=='__main__':
    rospy.init_node('transform')
    transform()
    rospy.spin()
