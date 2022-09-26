#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move_sq():
    # Starts a new node
    rospy.init_node('move_sq', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
 
    speed = 1
    distance = 2
    angle = 90
    


    #Since we are moving just in x-axis
    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
 
     #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        

        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
        #Publish the velocity
            velocity_publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)

        vel_msg.angular.z = speed
            

        
                #Since we are moving just in x-axis
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = angle

        




            while not rospy.is_shutdown():

            #Setting the current time for distance calculus
                t0 = rospy.Time.now().to_sec()

    #Converting from angles to radians
                angular_speed = speed*2*PI/360
                relative_angle = angle*2*PI/360
                current_angle = 0

                while(current_angle < relative_angle):
        
                    velocity_publisher.publish(vel_msg)
                    t1 = rospy.Time.now().to_sec()
            
                    current_angle = angular_speed*(t1-t0)

            #After the loop, stops the robot
        
        
        vel_msg.angular.z = 0
             #Force the robot to stop
        velocity_publisher.publish(vel_msg)
        rospy.spin()

if __name__ == '__main__':
    try:
    #Testing our function
       move_sq()
    except rospy.ROSInterruptException: 
        pass