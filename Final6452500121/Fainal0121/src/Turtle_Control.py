#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Int16
import os

frame = Tk()
frame.title("Turtle_Control")
frame.geometry("250x300")

mode = 1

def BTN(motion):
     if motion.data ==1:
        Forward()
        text = "Forward"
        pub_motion.publish(text)
     elif motion.data ==2:
        Backward()
        text = "Backward"
        pub_motion.publish(text)
     elif motion.data ==3:
        Turn_Left()
        text = "Turn Left"
        pub_motion.publish(text)
     elif motion.data ==4:
        Turn_Right()
        text = "Turn Right"
        pub_motion.publish(text)
        
pub_turtle = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
pub_motion = rospy.Publisher('motion', String, queue_size=10)
ledpub = rospy.Publisher("Topic_LED_13", Int16, queue_size = 10) 

if mode == 1:
    BTNsub = rospy.Subscriber("Status",Int16,callback=BTN)

rospy.init_node("Turtle_Control")
rate = rospy.Rate(10) # 10hz
def Forward():
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z= 0.0
    pub_turtle.publish(cmd)
    text = "Forward"
    pub_motion.publish(text)
        
def Backward():
    cmd = Twist()
    cmd.linear.x = -1.0
    cmd.angular.z= 0.0
    pub_turtle.publish(cmd)
    text = "Backword"
    pub_motion.publish(text)
       
def Turn_Left():
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= 1.0
    pub_turtle.publish(cmd)
    text = "Turn Left"
    pub_motion.publish(text)
   
def Turn_Right():
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= -1.0
    pub_turtle.publish(cmd)
    text = "Turn Right"
    pub_motion.publish(text)

def Talker(val):
	cmd_val = Int16(val)
	rospy.loginfo(cmd_val)
	ledpub.publish(cmd_val)
    
def on():
    os.system('rosservice call /turtle1/set_pen 255 255 255 3 0')
    Talker(1)
    text = "PenON"
    pub_motion.publish(text)

def off():
    os.system('rosservice call /turtle1/set_pen 255 255 255 3 1')
    Talker(0)
    text = "PenOFF"
    pub_motion.publish(text)

def mode():
    global mode
    mode = ~mode

B1 = Button(text = "Forward", command = Forward)
B1.place(x=73, y=20)

B2 = Button(text = "Backward", command = Backward)
B2.place(x=73, y=130)

B3 = Button(text = "Turn Left", command = Turn_Left)
B3.place(x=20, y=80)

B4 = Button(text = "Turn Right", command = Turn_Right)
B4.place(x=128, y=80)

B5 = Button(text = "Penon", command = on)
B5.place(x=20, y=200)

B6 = Button(text = "Penoff", command = off)
B6.place(x=73, y=200)

B7 = Button(text = "mode", command = mode)
B7.place(x=128, y=200)

frame.mainloop()    
    
    
    