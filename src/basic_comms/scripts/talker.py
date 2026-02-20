#!/usr/bin/env python
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('Talker')
    pub = rospy.Publisher("chatter", String, queue_size=1)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        global_str = rospy.get_param("/Message", "No Parameter found")
        msglobal = String()
        msglobal.data = global_str
        pub.publish(msglobal)

        local_str = rospy.get_param("Message", "No Parameter found")
        msglocal = String()
        msglocal.data = local_str
        pub.publish(msglocal)

        prv_str = rospy.get_param("~Message", "No Parameter found")
        msgprv = String()
        msgprv.data = prv_str
        pub.publish(msgprv)

        rate.sleep()