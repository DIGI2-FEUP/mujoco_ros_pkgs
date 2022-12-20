#!/usr/bin/python3

# Copyright 2018 Shadow Robot Company Ltd.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

import rospy
from mujoco_ros_msgs.srv import SpawnObjects
from object_recognition_msgs.msg import RecognizedObjectArray, RecognizedObject


class SpawnSimClient(object):
    """
    Dummy class to launch Mujoco simulation with objects
    """

    def __init__(self):
        self._sim_service = rospy.ServiceProxy("mujoco/spawn_sim_environment", SpawnObjects)

    def _request_sim(self, request):
        '''
        Service client that sends request to spawn simulation
        '''
        rospy.wait_for_service("mujoco/spawn_sim_environment", 15)
        try:
            response = self._sim_service(request)
            if response.success is True:
                rospy.loginfo("Sim environment successfully spawned!")
            return response.success
        except rospy.ServiceException as e:
            rospy.logerr("Service Call Failed:  %s" % e)

    def _send_request(self):
        request = RecognizedObjectArray()

        # Dummy obj 1
        #rec_object_1 = RecognizedObject()
        #rec_object_1.type.key = "base"
        #rec_object_1.pose.pose.pose.position.x = 0.1
        #rec_object_1.pose.pose.pose.position.y = 0.7
        #rec_object_1.pose.pose.pose.position.z = 0
        #rec_object_1.pose.pose.pose.orientation.x = 0.707
        #rec_object_1.pose.pose.pose.orientation.y = -0.707
        #rec_object_1.pose.pose.pose.orientation.z = 0
        #rec_object_1.pose.pose.pose.orientation.w = 0

        # Dummy obj 2
        #rec_object_2 = RecognizedObject()
        #rec_object_2.type.key = "base"
        #rec_object_2.pose.pose.pose.position.x = 0.3
        #rec_object_2.pose.pose.pose.position.y = 1
        #rec_object_2.pose.pose.pose.position.z = 0
        #rec_object_2.pose.pose.pose.orientation.x = 0.707
        #rec_object_2.pose.pose.pose.orientation.y = 0
        #rec_object_2.pose.pose.pose.orientation.z = 0
        #rec_object_2.pose.pose.pose.orientation.w = 0.707
        #request.objects = [rec_object_1, rec_object_2]
        self._request_sim(request)

if __name__ == '__main__':
    rospy.init_node("spawn_sim_client_example_node")
    spawn_sim = SpawnSimClient()
    spawn_sim._send_request()
    rospy.spin()
