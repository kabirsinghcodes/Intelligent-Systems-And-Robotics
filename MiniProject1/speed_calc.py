#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

# Define wheel radius (change as needed)
wheel_radius = 0.2  # in meters

def rpm_callback(msg):
    rpm = msg.data
    speed = (2 * 3.14159 * wheel_radius * rpm) / 60  # m/s
    
    speed_pub = rospy.Publisher('/speed', Float64, queue_size=10)
    speed_pub.publish(speed)
    
def speed_calc():
    rospy.init_node('speed_calc', anonymous=True)
    rospy.Subscriber('/rpm', Float64, rpm_callback)
    rospy.spin()
    
if __name__ == '__main__':
    speed_calc()
