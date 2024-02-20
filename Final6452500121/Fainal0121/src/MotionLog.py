#!/usr/bin/env python3
from tkinter import *
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Int16
import os

root = Tk()
root.geometry("300x300")
root.title(" Show Action ")

ledpub = rospy.Publisher("Topic_LED_13", Int16, queue_size = 10)

def clearToTextInput():
	ActOut.delete("1.0","end")
	ledpub.publish(1)
	os.system('rosservice call /reset')

def run(val):
	ActOut.insert(END, val.data + "\n")

if __name__ == "__main__":
	#  Initial ROS node and determine Publish or Subscribe action	
	sub = rospy.Subscriber("motion",String,callback=run)
	rospy.init_node("MotionLog")
	#rospy.spin()

	ActLabel = Label(text = "Motion", font = ("",18))
	ActLabel.place(x=113, y=10)
	ActOut = Text(root, height = 7, width = 10, bg = "light cyan", font = ("",16))
	ActOut.place(x=83, y=50)

	ClearBtn=Button(root,height=1,width=10,text="Clear",command=clearToTextInput)
	ClearBtn.place(x=103, y=250)

	mainloop()