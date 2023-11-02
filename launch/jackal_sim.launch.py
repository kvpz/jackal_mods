# this file is used to launch other launch files
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription 
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from launch_ros.actions import Node
import os 

def generate_launch_description():
    #params_file = PathJoinSubstitution([FindPackageShare('jackal_sim'),
    #                            'params', 'nav2_params.yaml'])

    launch_desc_cp_gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('clearpath_gz'),
                'launch',
                'simulation.launch.py'
            ])
        ]),
    )
    
    relative_path_to_clearpath_dir = os.path.join('')
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

    # declare_scanner_arg = DeclareLaunchArgument(
    #     name='scanner', default_value='scanner',
    #     description='Namespace for sample topics'
    # )

    # cloud_publisher_node = Node(
    #     package='pointcloud_to_laserscan', executable='dummy_pointcloud_publisher',
    #     remappings=[('cloud', '/sensors/lidar3d_0/points'), 
    #                 ('/scan', [LaunchConfiguration('scanner'), '/scan'])], # Keeping the original remapping for scan
    #                 # [LaunchConfiguration('scanner'), '/cloud'])],
    #     parameters=[{'cloud_frame_id': 'cloud', 'cloud_extent': 2.0, 'cloud_size': 500}],
    #     name='cloud_publisher'
    # )

    # static_transform_publisher_node = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',
    #     name='static_transform_publisher',
    #     arguments=[
    #         '--x', '0', '--y', '0', '--z', '0',
    #         '--qx', '0', '--qy', '0', '--qz', '0', '--qw', '1',
    #         '--frame-id', 'map', '--child-frame-id', 'cloud'
    #     ]
    # )

    # pointcloud_to_laserscan_node = Node(
    #     package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
    #     remappings=[('cloud_in', [LaunchConfiguration('scanner'), '/cloud']),
    #                 ('scan', [LaunchConfiguration('scanner'), '/scan'])],
    #     parameters=[{
    #         'target_frame': 'cloud',
    #         'transform_tolerance': 0.01,
    #         'min_height': 0.0,
    #         'max_height': 1.0,
    #         'angle_min': -1.5708,  # -M_PI/2
    #         'angle_max': 1.5708,  # M_PI/2
    #         'angle_increment': 0.0087,  # M_PI/360.0
    #         'scan_time': 0.3333,
    #         'range_min': 0.45,
    #         'range_max': 4.0,
    #         'use_inf': True,
    #         'inf_epsilon': 1.0
    #     }],
    #     name='pointcloud_to_laserscan'
    # )

    return LaunchDescription([
        # declare_scanner_arg,
        # cloud_publisher_node,
        # static_transform_publisher_node,
        # pointcloud_to_laserscan_node,
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
