# this file is used to launch nodes
import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

            Node(
                package='rtabmap_odom',
                executable='icp_odometry',
                name='icp_odometry',
                output='screen',
                parameters=[{
                    'scan_cloud_is_2d' : True,
                    'wait_imu_to_init' : True,
                    'use_sim_time': True,
                    #'laser_scan_topic' : '/scan',
                    #'odom_topic' : '/odom',
                    # 'publish_tf' : True,
                    'base_frame_id' : 'base_link',
                    #'odom_frame_id' : 'odom',
                    #'init_pose_from_topic' : '',
                    # 'freq' : 20.0}],
                    #'qos' : 0,
                    #'scan_range_min' : 0.2,
                    #'scan_range_max': 100.0
                }],
                remappings=[
                    #("scan_cloud", '/sensors/lidar3d_0/points')
                    #("scan", '/icp_scan_topic')
                    #("scan", '/scan'),
                    #("scan", '/sensors/lidar2d_0/scan'),
                    ("imu", '/sensors/imu_0/data')
                ],
            ),
    ])

# I have had success with the below using 2D lidar laserscan data. 

            # Node(
            #     package='rtabmap_odom',
            #     executable='icp_odometry',
            #     name='icp_odometry',
            #     output='screen',
            #     parameters=[{
            #         'scan_cloud_is_2d' : True,
            #         'use_sim_time': True,
            #         'base_frame_id' : 'base_link',
            #     }],
            #     remappings=[
            #         ("scan", '/icp_scan_topic')
            #     ],
            # ),