环境要求
- Ubuntu 22.04 + ROS2 Humble
- Python 3.8+
- colcon
克隆与编译
克隆:git clone https://github.com/sail1106/CQJTU_RM2026-phase_0-.git
cd CQJTU_RM2026-phase_0-
编译:colcon build --packages-select my_robot_msgs demo_py_pkg
source install/setup.bash
分别在两个终端里面先编译后运行publisher:ros2 run demo_py_pkg publisher
subscriber:ros2 run demo_py_pkg subscriber
自定义消息为：点（x , y）以y=2x的函数的变化规律发送“hello x”
