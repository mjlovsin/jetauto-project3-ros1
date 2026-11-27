# Launch and Run Instructions

## 1. Connect to JetAuto

From Ubuntu VM:

```bash
ssh jetauto@192.168.149.1
```

## 2. Start ROS Master

**SSH Terminal 1:**

```bash
source /opt/ros/melodic/setup.bash
source ~/jetauto_ws/devel/setup.bash
roscore
```

Keep terminal running. Skip if ROS master is already running.

## 3. Start Motor Controller

**SSH Terminal 2:**

```bash
ssh jetauto@192.168.149.1
```

```bash
source /opt/ros/melodic/setup.bash
source ~/jetauto_ws/devel/setup.bash
```

```bash
export PYTHONPATH=/home/jetauto/jetauto_ws/src/jetauto_driver/jetauto_sdk/src:$PYTHONPATH
```

```bash
roslaunch jetauto_controller jetauto_controller.launch
```

Keep terminal running.

## 4. Transfer Python Controller

**Ubuntu VM:**

```bash
cd ~/jetauto-project3-ros1
```

```bash
scp scripts/jetauto_control_ros1.py jetauto@192.168.149.1:~/
```

## 5. Verify Controller Connection

**SSH Terminal 3:**

```bash
ssh jetauto@192.168.149.1
```

```bash
source /opt/ros/melodic/setup.bash
source ~/jetauto_ws/devel/setup.bash
```

```bash
rostopic info /jetauto_controller/cmd_vel
```

Expected:

```text
Type: geometry_msgs/Twist

Subscribers:
 * /jetauto_controller
```

## 6. Run Movement Sequence

Ensure the robot is in a clear area with an emergency stop accessible. For initial testing, safely raise the wheels.

```bash
python ~/jetauto_control_ros1.py
```

## 7. Update and Rerun

**Ubuntu VM:**

```bash
scp ~/jetauto-project3-ros1/scripts/jetauto_control_ros1.py jetauto@192.168.149.1:~/
```

**JetAuto SSH Terminal:**

```bash
python ~/jetauto_control_ros1.py
```

No ROS restart required if the master and motor controller remain running.

## Notes

- ROS 1 Melodic
- Ubuntu 18.04 on JetAuto
- No ROS bridge or NoMachine required
- No additional installation required
- Uses `/jetauto_controller/cmd_vel`
- Movement is time-based
- Avoid running multiple movement controllers simultaneously
