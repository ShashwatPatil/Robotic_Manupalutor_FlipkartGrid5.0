import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_SGP', anonymous=True)

robot_SGP = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group_name = "SGP_robotic_arm"
group = moveit_commander.MoveGroupCommander(group_name)

# We can get the name of the reference frame for this robot:
planning_frame = group.get_planning_frame()
print("============ Reference frame: %s" % planning_frame)

# We can also print the name of the end-effector link for this group:
eef_link = group.get_end_effector_link()
print("============ End effector: %s" % eef_link)

# We can get a list of all the groups in the robot:
group_names = robot_SGP.get_group_names()
print("============ Robot Groups:", robot_SGP.get_group_names())

# Sometimes for debugging it is useful to print the entire state of the
# robot:
print("============ Printing robot state")
print(robot_SGP.get_current_state())
print("")

joint_goal = group.get_current_joint_values()
print(joint_goal,"\n this is it")
joint_goal[0] = 0
joint_goal[1] = 1
joint_goal[2] = pi/2
joint_goal[3] = 3

# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
group.go(joint_goal, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
group.stop()

print("Exicuted!!!!")

