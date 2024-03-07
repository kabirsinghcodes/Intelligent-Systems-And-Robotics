import rospy

if __name__ == "__main__":
    rospy.init_node('first_node')
    rospy.loginfo("this node has started running")
    rospy.sleep(1)
    rospy.loginfo("Exit Now")