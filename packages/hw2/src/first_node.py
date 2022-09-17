#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def turtle_sq():
    rospy.init_node('first_node', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    
    while not rospy.is_shutdown():
      vel.linear.x = 1
      vel.linear.y = 0
      vel.linear.z = 0
      vel.angular.x = 0
      vel.angular.y = 0
      vel.angular.z = 0
      pub.publish(vel)
      rate.sleep()


if __name__ == '__main__':
   try:
     turtle_sq()
   except rospy.ROSInterruptException:
     pass
