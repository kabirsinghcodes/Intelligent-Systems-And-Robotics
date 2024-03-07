#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def rpm_publisher():
    rospy.init_node('rpm_publisher', anonymous=True)
    rpm_pub = rospy.Publisher('/rpm', Float64, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz publishing rate
    
    rpm_value = 900.0  # Constant RPM value (change as needed)
    
    while not rospy.is_shutdown():
        rpm_pub.publish(rpm_value)
        rate.sleep()
    
if __name__ == '__main__':
    try:
        rpm_publisher()
    except rospy.ROSInterruptException:
        pass
