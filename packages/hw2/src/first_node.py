import rospy
from geometry_msgs.msg import Twist
import sys
pi = 3.141592653589
​
def turtle_sq():
	rospy.init_node('turtlesim_sq', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
	rate = rospy.Rate(10)
	vel = Twist()
	
	#1
	t = 0
	while t < 20:
	    vel.linear.x = 0.1
	    vel.linear.y = 0
	    vel.linear.z = 0
	    vel.angular.x = 0
	    vel.angular.y = 0
	    vel.angular.z = 0
	    pub.publish(vel)
	    rate.sleep()
	    t = t + 0.1
	    
	#2
​
	t = 0
	while t<10:
	    vel.linear.x = 0
	    vel.linear.y = 0
	    vel.linear.z = 0
	    vel.angular.x = 0
	    vel.angular.y = 0
	    vel.angular.z = pi/2
	    pub.publish(vel)
	    rate.sleep()	
	    t = t + 0.1	
​
	t = 0#3
	while t < 20:
	    vel.linear.x = 0.1
	    vel.linear.y = 0
	    vel.linear.z = 0
	    vel.angular.x = 0
	    vel.angular.y = 0
	    vel.angular.z = 0
	    pub.publish(vel)
	    rate.sleep()	
	    t = t + 0.1
	
	t = 0#4
	while t<10:
	    vel.linear.x = 0
	    vel.linear.y = 0
	    vel.linear.z = 0
	    vel.angular.x = 0
	    vel.angular.y = 0
	    vel.angular.z = pi/2
	    pub.publish(vel)
	    rate.sleep()	
	    t = t + 0.1	
	   	
	t=0#5
	while t < 20:
	    vel.linear.x = 0.1
	    vel.linear.y = 0
	    vel.linear.z = 0
	    vel.angular.x = 0
	    vel.angular.y = 0
	    vel.angular.z = 0
	    pub.publish(vel)
	    rate.sleep()
	    t = t + 0.1
	   
	t =0#6
	while t<10:
	    vel.linear.x = 0
	    vel.linear.y = 0
	    vel.linear.z = 0
	    vel.angular.x = 0
	    vel.angular.y = 0
	    vel.angular.z = pi/2
	    pub.publish(vel)
	    rate.sleep()	
	    t = t + 0.1	
	    
	t =0#7
	while t < 20:
	    vel.linear.x = 0.1
	    vel.linear.y = 0
	    vel.linear.z = 0
	    vel.angular.x = 0
	    vel.angular.y = 0
	    vel.angular.z = 0
	    pub.publish(vel)
	    rate.sleep()
	    t = t + 0.1
​
if __name__ == '__main__':
	try:
		turtle_sq()
	except rospy.ROSInterruptException:
		pass
