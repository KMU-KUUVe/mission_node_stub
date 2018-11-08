#!/usr/bin/env python
import rospy
import actionlib 
from darknet_ros_msgs.msg import CheckForObjectsAction, CheckForObjectsGoal, CheckForObjectsResult, CheckForObjectsFeedback, BoundingBox

class SignNodeStub:
	_result = CheckForObjectsResult()

	def __init__(self):
		self._action_name = rospy.get_name()
		self._as = actionlib.SimpleActionServer(self._action_name, CheckForObjectsAction, execute_cb=self.actionCallback, auto_start = False)
		self._as.start()
		
		self.box_class = rospy.get_param("~box_class")
		self.box_probability = rospy.get_param("~box_probability")


	def actionCallback(self, goal):
		rospy.loginfo("%s, actionCallback called!" % self._action_name)
		rospy.loginfo("%s, class: %s, probability: %f" % (self._action_name, self.box_class, self.box_probability))
		bounding_box = BoundingBox()
		bounding_box.Class = self.box_class
		bounding_box.probability = self.box_probability

		rospy.sleep(1.)		# sleep for 1 sec

		self._result.bounding_boxes[0] = bounding_box
		rospy.loginfo('%s: send return!' % self._action_name)
		rospy.loginfo('-------------------------------')
		self._as.set_succeeded(self._result)


if __name__ == '__main__':
	rospy.init_node('sign_stub_node', anonymous=True)	
	try: 
		sign_node_stub = SignNodeStub()
		rospy.spin()	
		
	except rospy.ROSInterruptException:
		print(error)
		pass			
			