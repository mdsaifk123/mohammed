#!/usr/bin/env python
   2 import rospy
   3 from geometry_msgs.msg import Twist
   4 
   5 def move():
   6     # Starts a new node
   7     rospy.init_node('robot_cleaner', anonymous=True)
   8     velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
   9     vel_msg = Twist()
  10 
  11     #Receiveing the user's input
  12     print("Let's move your robot")
  13     speed = input("Input your speed:")
  14     distance = input("Type your distance:")
  15     isForward = input("Foward?: ")#True or False
  16 
  17     #Checking if the movement is forward or backwards
  18     if(isForward):
  19         vel_msg.linear.x = abs(speed)
  20     else:
  21         vel_msg.linear.x = -abs(speed)
  22     #Since we are moving just in x-axis
  23     vel_msg.linear.y = 0
  24     vel_msg.linear.z = 0
  25     vel_msg.angular.x = 0
  26     vel_msg.angular.y = 0
  27     vel_msg.angular.z = 0
  28 
  29     while not rospy.is_shutdown():
  30 
  31         #Setting the current time for distance calculus
  32         t0 = rospy.Time.now().to_sec()
  33         current_distance = 0
  34 
  35         #Loop to move the turtle in an specified distance
  36         while(current_distance < distance):
  37             #Publish the velocity
  38             velocity_publisher.publish(vel_msg)
  39             #Takes actual time to velocity calculus
  40             t1=rospy.Time.now().to_sec()
  41             #Calculates distancePoseStamped
  42             current_distance= speed*(t1-t0)
  43         #After the loop, stops the robot
  44         vel_msg.linear.x = 0
  45         #Force the robot to stop
  46         velocity_publisher.publish(vel_msg)
  47 
  48 if __name__ == '__main__':
  49     try:
  50         #Testing our function
  51         move()
  52     except rospy.ROSInterruptException: pass
