#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float32

i = 0.0

if __name__=='__main__':
    rospy.init_node("signal_generator")
    Hrtz = rospy.get_param("/Hrtz_Rate", 10)
    Inc = rospy.get_param("~Resolution", 0.1)
    rate = rospy.Rate(Hrtz)
    signal_pub = rospy.Publisher("Signal", Float32, queue_size = 1)
    time_pub = rospy.Publisher("Timer", Float32, queue_size = 1)

    while not rospy.is_shutdown():
        fsin = np.sin(np.pi*i/180)
        msg1 = Float32()
        msg1.data = fsin
        signal_pub.publish(msg1)

        msg2 = Float32()
        msg2.data = i
        time_pub.publish(msg2)
        i += Inc

        rate.sleep()