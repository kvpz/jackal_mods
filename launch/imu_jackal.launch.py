# this file is used to launch other launch files
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
import os

def generate_launch_description():
    params_file = PathJoinSubstitution([FindPackageShare('jackal_sim'),
                                'params', 'nav2_params.yaml'])

    launch_desc_cp_gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('clearpath_gz'),
                'launch',
                'simulation.launch.py'
            ])
        ]),
    )
    
    launch_desc_cp_demo_local = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('clearpath_nav2_demos'),
                'launch',
                'localization.launch.py'
            ])
        ]),
        launch_arguments={
            'setup_path': os.path.expanduser('~/clearpath/'),
            'use_sim_time': 'true'
        }.items()
    )

    launch_desc_cp_demo_nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('clearpath_nav2_demos'),
                'launch',
                'nav2.launch.py'
            ])
        ]),
        launch_arguments={
            'setup_path': os.path.expanduser('~/clearpath/'),
            'use_sim_time': 'true'
        }.items()
    )

    launch_desc_cp_viz_viewnav = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('clearpath_viz'),
                'launch',
                'view_navigation.launch.py'
            ])
        ]),
    )

    return LaunchDescription([
        launch_desc_cp_gz_sim,
        launch_desc_cp_demo_local,
        launch_desc_cp_demo_nav2,
        launch_desc_cp_viz_viewnav
    ])

    # return LaunchDescription([
    #     IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource([
    #             PathJoinSubstitution([
    #                 FindPackageShare('nav2_bringup'),
    #                 'launch',
    #                 'navigation_launch.py'
    #             ])
    #         ]),
    #         launch_arguments={
    #             'params_file': params_file,
    #         }.items()
    #     )
    # ])
