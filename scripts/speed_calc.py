import rospy
from std_msgs.msg import Float32

wheel_radius = rospy.get_param("/wheel_radius")

def calc_speed(rpm, publisher):
    wheel_radius = rospy.get_param("/wheel_radius")
    speed = rpm.data * 2 * 3.14159 / 60 * wheel_radius
    publisher.publish(speed)

def create_subscriber(pub):
    rospy.Subscriber("rpm", Float32, calc_speed, (pub))

def speed_pub():
    pub = rospy.Publisher("speed", Float32, queue_size=10)
    return pub

if __name__ == '__main__':
    rospy.init_node("speed_calc_sub_node")
    pub = speed_pub()
    create_subscriber(pub)
    rospy.spin() 