#!/usr/bin/env python3

import rospy


if rospy.has_pram("mode"):
    self.foo = rospy.get_pram("mode")
else:
    self.foo = "default"