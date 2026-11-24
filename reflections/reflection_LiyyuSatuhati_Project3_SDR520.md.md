# Project 3: Real-world JetAuto motion control, reflection and calibration

## Final parameters and calibration table

These values come from `jetauto_control_ros1.py`. The commanded result is velocity times duration.

| Motion | Velocity command | Final tuned time | Commanded result 
|---|---|---:|---
| Forward | `linear.x = 0.2` m/s | 6.0 s | 1.2 m 
| Left sideways | `linear.y = +0.2` m/s | 6.0 s | 1.2 m 
| Clockwise turn | `angular.z = -1.0` rad/s | 1.55 s | 1.55 rad (about 88.8°) 
| Right sideways | `linear.y = -0.2` m/s | 6.0 s | 1.2 m 
| Arc rotation | `angular.z = -1.0` rad/s | 0.6 s | 0.6 rad (about 34°) 
| Forward + turn (return) | `linear.x = 0.2`, `angular.z = +0.2` | 6.75 s | 1.35 m, 1.35 rad (about 77°) 
| Turn back to starting heading | `angular.z = +1.0` rad/s | 1.25 s | 1.25 rad (about 71.6°) 

Each segment is followed by a 1.0 s pause with a zero-velocity stop. Commands are published at 10 Hz (`time.sleep(0.1)`).

Adjustments: the clockwise rotation was cut from 1.76 s in the simulated model to 1.55 s on the real robot, because the longer time over-turned and the path was not square. It could probably go down to about 1.4 s.

Observation: the robot drove a recognizable square. It ended very close to the intended position, but its final heading was slightly off, so the motion was not perfectly repeatable from run to run. The distances were judged by eye and not measured with a tape.

## Reflection answers

**1. How did you establish communication with the robot?**

We joined the robot's Wi-Fi network from an Ubuntu VM running in VirtualBox and connected to the JetAuto over SSH (`ssh jetauto@192.168.149.1`). On the robot we sourced ROS Melodic and the `~/jetauto_ws` workspace. We started `roscore` in one SSH terminal, then added the JetAuto SDK to `PYTHONPATH` and ran `roslaunch jetauto_controller jetauto_controller.launch` in a second. We copied the control script to the robot with `scp` and ran it there, so the ROS master and the script were on the same machine. We did not need a ROS bridge or a remote desktop.

**2. Which velocity command topic did your robot use?**

`/jetauto_controller/cmd_vel`, not the generic `/cmd_vel`.

**3. How did you verify the message type expected by the robot?**

We ran `rostopic info /jetauto_controller/cmd_vel` in a third SSH terminal. It reported the type `geometry_msgs/Twist` and listed `/jetauto_controller` as the subscriber. That confirmed the message type and that the hardware controller was listening before we ran any motion code.

**4. What final velocity and duration values did you use for each segment?**

See the calibration table. Forward, left, and right all used 0.2 m/s for 6.0 s. In-place rotations used 1.0 rad/s for 1.55 s (clockwise turn), 0.6 s (arc rotation), and 1.25 s (turn back). The combined move used 0.2 m/s forward and 0.2 rad/s for 6.75 s.

**5. How close was the robot to the intended 1-meter motion segments?**

Pretty close. We did not measure with a tape, so this is a visual estimate: each segment looked about right, and the robot traced a square that our instructor accepted as close enough. The robot finished very near the intended end position, but its final heading was off.

The commanded distance is not exactly 1 m. At a constant 0.2 m/s, a 6 s translation nominally covers 1.2 m. That calculation does not show how far the robot really travelled.

**6. How did Gazebo or simulation timing differ from physical robot timing, if you tested both?**

We tested in simulation first, and the timings did not carry over exactly. The clockwise turn used 1.76 s in the simulated model, but on the real robot that over-turned and the path no longer lined up as a square, so we dropped it to 1.55 s. It could likely go to about 1.4 s. A simulator applies the commanded velocity almost exactly, while the real robot accelerates gradually and is affected by floor friction, so its timings had to be tuned by watching it.

**7. Which motion segment was hardest to tune: forward, lateral, turn, or combined motion? Why?**

The arc, meaning the combined forward-and-turn return move. We kept adjusting its time, the initial rotation angle before it, and the constant turning radius during it. After it we also had to adjust by eye to bring the robot back to square for the reset, which is why the script has a separate arc rotation step (0.6 s), a 6.75 s combined move, and a turn-back step (1.25 s). Errors in position and heading from the earlier segments carry into this move, and a curved path is harder to judge than a straight one.

**8. What real-world effects caused error or drift?**

The main factor we saw was the floor: a slippery or uneven surface lets the wheels slip. Our classroom floor is poured concrete, which is probably the best surface we could have found for the demonstration, so the error would likely be larger on other floors.

Other likely contributors, which we did not isolate:
- Mecanum sideways motion is less efficient and less repeatable than forward motion.
- Battery level can change the motor response between runs.
- The robot does not reach the commanded speed or stop instantly, and the script has no feedback to correct for that.
- Timing jitter from `time.sleep` loops running over SSH on a non-real-time OS.
- Open-loop error builds up across segments and across repetitions, because nothing resets the position.

**9. What safety precautions did your team follow?**

- We cleared the area the robot was expected to travel through and made sure nobody was near it who could trip over it.
- We kept the emergency stop accessible, and a teammate was ready to pick the robot up if it started driving into something.
- The first tests were done with the wheels raised, as the README says.
- Only one movement controller ran at a time, so commands could not conflict.
- The script sends a zero-velocity `Twist` after every segment, in a `finally` block, and on ROS shutdown (`rospy.on_shutdown`), so Ctrl+C stops the robot.

**10. If you had more time, how would you improve the controller?**

- Make the robot finish completely square. It ended very close to the intended position, but the final rotation was off.
- Use odometry or encoder feedback so each segment ends when the measured distance or angle is reached, instead of after a fixed time.
- Move the tuned values into ROS parameters or a YAML file with a launch file, so retuning does not mean editing code.
- Add a start countdown and a safety timeout.
- Log each executed segment, and measure the real end poses against floor markers to build a proper error table.
- Add acceleration ramps to reduce slip at the start and end of each segment.

