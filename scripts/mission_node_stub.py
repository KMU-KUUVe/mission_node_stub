#!/usr/bin/env python
import rospy
import actionlib 
from mission_planner.msg import MissionPlannerAction, MissionPlannerGoal, MissionPlannerResult, MissionPlannerFeedback

class MissionNodeStub:
    _result = MissionPlannerResult()

    def __init__(self):
        self._action_name = rospy.get_name()
        self._as = actionlib.SimpleActionServer(self._action_name, MissionPlannerAction, execute_cb=self.actionCallback, auto_start = False)
        self._as.start()


    def actionCallback(self, goal):
        rospy.loginfo("%s, actionCallback called!" % self._action_name)

        rospy.sleep(3.)		# sleep for 1 sec

        rospy.loginfo('%s: send return!' % self._action_name)
        rospy.loginfo('-------------------------------')
        self._as.set_succeeded(self._result)


if __name__ == '__main__':
    rospy.init_node('mission_stub_node', anonymous=True)	
    try: 
        mission_node_stub = MissionNodeStub()
        rospy.spin()	
		
    except rospy.ROSInterruptException:
        print(error)
        pass			
			
