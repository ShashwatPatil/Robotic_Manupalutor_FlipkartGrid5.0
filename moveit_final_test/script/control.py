import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import serial 
import time 

# arduino comms setup
# arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1) 

# def write_read(x): 
#     arduino.write(bytes(x,'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()  ## waaithing te get a response of a target pose being succesfullly used #will prevent it from overflowing
#     return data

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_SGP', anonymous=True)

robot_SGP = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group_name = "SGP_robotic_arm"
group = moveit_commander.MoveGroupCommander(group_name)

# def moveto_pose_using_path(path):
    


def move_joint_angles(a1,a2,a3,a4):
    joint_goal = group.get_current_joint_values()
    print(joint_goal,"\n this is it")
    joint_goal[0] = a1
    joint_goal[1] = a2
    joint_goal[2] = a3
    joint_goal[3] = a4

    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    group.go(joint_goal, wait=True)

    # Calling ``stop()`` ensures that there is no residual movement
    group.stop()

    group.clear_pose_targets()
    
    print("Exicuted!!!!")


def goto_pose(cx=-8.138761369766284e-05,cy=1.186,cz=1.26,qx=-0.3662010712722356,qy=-1.2333012995064459e-05,qz=3.251175267868647e-05,w=0.9305357457883872):
    pose_goal = moveit_msgs
    pose_goal.orientation.x = qx
    pose_goal.orientation.y = qy
    pose_goal.orientation.z = qz
    pose_goal.orientation.w = w
    pose_goal.position.x = cx
    pose_goal.position.y = cy
    pose_goal.position.z = cz
    pose_goal = group.get_current_pose()
    a = pose_to_list(pose_goal)
    print(a)
    print(pose_goal)
    group.set_pose_target(pose_goal)
    # `go()` returns a boolean indicating whether the planning and execution was successful.
    success = group.go(wait=True)
    # Calling `stop()` ensures that there is no residual movement
    group.stop()
    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets().
    group.clear_pose_targets()



def predefined_pose(name):
    pose_goal = geometry_msgs.msg.Pose()
    print("Current pose. pose ")
    print(group.get_current_pose().pose)
    print("current pose ")
    print(group.get_current_pose())
    group.set_named_target(name)
    plan = group.go(wait=True)
    # Calling `stop()` ensures that there is no residual movement
    group.stop()
    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets()
    group.clear_pose_targets()
    print("Exicuted!!!")
    print("Current pose")
    print(group.get_current_pose().pose)


def cartesian_path(scale=1):
    waypoints = []

    wpose = group.get_current_pose().pose
    wpose.position.z -= scale * 0.5  # First move up (z)
    wpose.position.y += scale * 0.7  # and sideways (y)
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.x += scale * 0.3  # Second move forward/backwards in (x)
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.y -= scale * 0.4  # Third move sideways (y)
    waypoints.append(copy.deepcopy(wpose))

    # We want the Cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in Cartesian
    # translation.  We will disable the jump threshold by setting it to 0.0,
    # ignoring the check for infeasible jumps in joint space, which is sufficient
    # for this tutorial.
    (plan, fraction) = group.compute_cartesian_path(
        waypoints, 0.1, 0.0  # waypoints to follow  # eef_step
    )  # jump_threshold

    # Note: We are just planning, not asking move_group to actually move the robot yet:
    return plan, fraction



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
print("SGP")

# move_joint_angles(-pi/2,-pi/4,pi/20,pi/3)

# predefined_pose("drop")
# rospy.sleep(1.5)
# print("Cartasian")
# path_cart, fraction = cartesian_path(100)
# print(path_cart,"\n\n",fraction)
# group.execute(path_cart, wait=True)
# print("Pose using coordinates \n")
goto_pose()
