#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float32

signal = 0.0
i = 0.0

def callback1(msg1):
    global signal
    signal = msg1.data

def callback2(msg2):
    global i
    i = msg2.data

if __name__=='__main__':
    rospy.init_node("process")
    Hrtz = rospy.get_param("/Hrtz_Rate", 10)
    phasing = rospy.get_param("~Phasing", 0.05)
    scaling = rospy.get_param("~Scaling", 1.5)
    rate = rospy.Rate(Hrtz)  
    signal_sub = rospy.Subscriber("Signal", Float32, callback1)
    timer_sub = rospy.Subscriber("Timer", Float32, callback2)
    pro_signal_pub = rospy.Publisher("Processed_Signal", Float32, queue_size = 1)

    while not rospy.is_shutdown():
        fsin = ((signal * np.cos(np.pi*(phasing)/180)) + (np.sin(np.pi*(phasing)/180)*np.cos(np.pi*i/180)))*scaling
        msg3 = Float32()
        msg3.data = fsin
        pro_signal_pub.publish(msg3)

        rate.sleep()

    rospy.spin()