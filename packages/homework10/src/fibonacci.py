#!/usr/bin/env python3
import sys
import rospy
from example_service.srv import Fibonacci, FibonacciResponse
import example_action_server.msg 
import actionlib


class Homework10:
    
    def Fibonacci_client(order):
        rospy.wait_for_service('/calc_fibonacci')   
        try:
           s1 = rospy.ServiceProxy('/calc_fibonacci',Fibonacci)
           resp1=s1(order)
           rospy.loginfo("The sequence is :  "+str(resp1))
           return resp1
           
        except rospy.ServiceException as e:
           print("Service call failed: %s"%e)
           
    def Fibonacci_client_action():
        client = actionlib.SimpleActionClient('/fibonacci',example_action_server.msg.FibonacciAction)
        client.wait_for_server()
        
        
        set_1 = example_action_server.msg.FibonacciGoal(order=3)
        client.send_goal(set_1)
        client.wait_for_result()
        #client.get_result()
        rospy.loginfo("The Action_sequence is  :  "+str(client.get_result()))
        set_2 = example_action_server.msg.FibonacciGoal(order=15)
        client.send_goal(set_2)
        client.wait_for_result()
        #client.get_result()
        rospy.loginfo("The Action_sequence is  :  "+str(client.get_result()))
        
        
        
    if __name__ == '__main__':
        rospy.init_node('Homework10')
        
        Fibonacci_client(3)
        Fibonacci_client(15)  
        Fibonacci_client_action()
         