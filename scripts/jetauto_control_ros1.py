#!/usr/bin/env python
from __future__ import print_function

import time
import rospy
from geometry_msgs.msg import Twist


class JetAutoControl:
    def __init__(self):
        rospy.init_node('jetauto_control')

        self.publisher = rospy.Publisher(
            '/jetauto_controller/cmd_vel',
            Twist,
            queue_size=10
        )

        rospy.on_shutdown(self.stop)
        rospy.loginfo('JetAuto controller started')

    def stop(self):
        self.publisher.publish(Twist())

    def move(self, x, y, z, duration):
        msg = Twist()

        msg.linear.x = float(x)
        msg.linear.y = float(y)
        msg.angular.z = float(z)

        start_time = time.time()

        try:
            while (
                not rospy.is_shutdown()
                and time.time() - start_time < duration
            ):
                self.publisher.publish(msg)
                time.sleep(0.1)
        finally:
            self.stop()


def main():
    node = JetAutoControl()

    try:
        # Allow ROS publisher to connect
        time.sleep(1.0)

        rospy.loginfo('Moving forward')
        node.move(0.2, 0.0, 0.0, 6.0)

        time.sleep(1.0)

        rospy.loginfo('Moving left')
        node.move(0.0, 0.2, 0.0, 6.0)

        time.sleep(1.0)

        rospy.loginfo('Rotating clockwise')
        node.move(0.0, 0.0, -1.0, 1.55)

        time.sleep(1.0)

        rospy.loginfo('Moving right')
        node.move(0.0, -0.2, 0.0, 6.0)

        time.sleep(1.0)

        rospy.loginfo('Rotating for arc')
        node.move(0.0, 0.0, -1.0, 0.6)

        time.sleep(1.0)

        rospy.loginfo('Returning to start')
        node.move(0.2, 0.0, 0.2, 6.75)

        time.sleep(1.0)

        rospy.loginfo('Turning back to norm')
        node.move(0.0, 0.0, 1.0, 1.25)

    except (KeyboardInterrupt, rospy.ROSInterruptException):
        pass

    finally:
        node.stop()


if __name__ == '__main__':
    main()
