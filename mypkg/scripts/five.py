#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

n = 0

def cb(message):
    global n
    n = message.data*5

if __name__ == '__main__': 
    rospy.init_node('five')
    sub = rospy.Subscriber('count_up', Float64, cb) 
    pub = rospy.Publisher('five', Float64, queue_size=1) 
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
 
 
