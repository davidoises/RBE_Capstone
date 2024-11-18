#!/usr/bin/env python

import rospy

from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class object_detector:
    def __init__(self):
        sub_topic_name="/realsense/image_raw"
        self.camera_subscriber = rospy.Subscriber(sub_topic_name, Image, self.camera_cb)
        self.bridge = CvBridge()    

    def camera_cb(self, data):
        img = self.bridge.imgmsg_to_cv2(data, "bgr8")
        cv2.imshow("output", img)
        cv2.waitKey(1)

if __name__ == '__main__':
    node_name = "object_detector"
    rospy.init_node(node_name)
    object_detector()
    rospy.spin()