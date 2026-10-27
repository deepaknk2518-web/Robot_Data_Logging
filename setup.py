from setuptools import find_packages, setup

package_name = 'robot_monitor_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sri',
    maintainer_email='srilusid2353@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		'robot_publisher=robot_monitor_pkg.robot_publisher:main',
		'robot_data=robot_monitor_pkg.robot_data:main',

        ],
    },
)
