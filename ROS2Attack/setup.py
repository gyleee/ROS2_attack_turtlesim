from setuptools import setup

package_name = 'ROS2Attack'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vcs',
    maintainer_email='vcs@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtlesim_publisher = ROS2Attack.turtlesim_publiser:main',
            'turtlesim_subscriber = ROS2Attack.turtlesim_subscriber:main'
        ],
    },
)
