import launch.actions
import launch_ros.actions
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        launch.actions.LogInfo(
            msg="Launch ROS2 turtorial cpp pubsub"),
        launch.actions.TimerAction(period=3.0,actions=[
            launch.actions.LogInfo(
                msg="It's been three minutes scince the launch."),
            ]),

        Node(
            package='ros2_cpp_pubsub',
            executable='talker',
            name='cpp_pubsub_publisher',
        ),
        Node(
            package='ros2_cpp_pubsub',
            executable='listener',
            name='cpp_pubsub_subscriber',
        ),
    ])

