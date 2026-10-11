from setuptools import find_packages, setup

package_name = 'rt2_nodes'

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
    maintainer='adithi',
    maintainer_email='adithi@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'node1 = rt2_nodes.node1:main',
            'node2 = rt2_nodes.node2:main',
            'node3 = rt2_nodes.node3:main',

        ],
    },
)
