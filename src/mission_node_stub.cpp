#include "mission_node_stub/mission_node_stub.h"
#include <string>

using namespace std;

MissionNodeStub::MissionNodeStub(char* action_name)
    : as_(nh_, string(action_name), boost::bind(&MissionNodeStub::actionCallback, this, _1), false),  action_name_(action_name)
{
    nh_ = ros::NodeHandle("~");

	as_.start();
}

void MissionNodeStub::actionCallback(const state_cpp_msg::MissionPlannerGoalConstPtr& goal)
{
    ROS_INFO("%s, actioncallback called!", action_name_);

    ros::Duration(1).sleep();       // sleep for 1 sec

    ROS_INFO("%s, send return!", action_name_);
    ROS_INFO("---------------------------");

    state_cpp_msg::MissionPlannerResult result;
	as_.setSucceeded(result);
}
