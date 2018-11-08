#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include "state_cpp_msg/MissionPlannerAction.h"

#ifndef MISSION_NODE_STUB_H
#define MISSION_NODE_STUB_H

class MissionNodeStub
{
public:
    MissionNodeStub(char* action_name);

    void actionCallback(const state_cpp_msg::MissionPlannerGoalConstPtr& goal);

protected:
    ros::NodeHandle nh_;

    actionlib::SimpleActionServer<state_cpp_msg::MissionPlannerAction> as_;

    char* action_name_;
};

#endif