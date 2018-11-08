#include <ros/ros.h>
#include "mission_node_stub/mission_node_stub.h"
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
    ros::init(argc, argv, "mission_node_stub");  // will be changed by launch file

    char* action_name = argv[1]; // To make multi node
    
    MissionNodeStub mission_node_stub(action_name);


	ros::spin();
	return 0;
}
