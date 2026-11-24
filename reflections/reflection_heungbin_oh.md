# Project 3 Reflection

1. **How did you establish communication with the robot?**  
   The README describes connecting from an Ubuntu VM to the JetAuto over SSH at `192.168.149.1`, starting ROS and the motor controller, and transferring the controller script with `scp`. The script publishes velocity commands through ROS.

2. **Which velocity command topic did your robot use?**  
   `/jetauto_controller/cmd_vel`.

3. **How did you verify the message type expected by the robot?**  
   The README says to run `rostopic info /jetauto_controller/cmd_vel`. The expected output lists `geometry_msgs/Twist` as the message type and `/jetauto_controller` as a subscriber.

4. **What final velocity and duration values did you use for each segment?**  
   The repository controller contains these values. I can't confirm whether these are the final values used during the physical test.

   | Segment | Linear x (m/s) | Linear y (m/s) | Angular z (rad/s) | Duration |
   |---|---:|---:|---:|---:|
   | Forward | 0.2 | 0.0 | 0.0 | 6.0 s |
   | Left | 0.0 | 0.2 | 0.0 | 6.0 s |
   | Clockwise rotation | 0.0 | 0.0 | -1.0 | 1.55 s |
   | Right | 0.0 | -0.2 | 0.0 | 6.0 s |
   | Rotation for arc | 0.0 | 0.0 | -1.0 | 0.6 s |
   | Combined return | 0.2 | 0.0 | 0.2 | 6.75 s |
   | Turn back to normal | 0.0 | 0.0 | 1.0 | 1.25 s |

5. **How close was the robot to the intended 1-meter motion segments?**  
   We haven't measured the actual distance. At a constant 0.2 m/s, a 6-second translation would nominally cover 1.2 m, but this calculation does not show how far the physical robot actually traveled.

6. **How did Gazebo or simulation timing differ from physical robot timing, if you tested both?**  
   The movement loop uses Python's `time.time()` and timed sleeps. The repository does not document a Gazebo test or a comparison between simulation and physical robot timing.

7. **Which motion segment was hardest to tune: forward, lateral, turn, or combined motion? Why?**  
   Turning and forward motion were the hardest to tune because wheel friction caused the robot to follow a curved path instead of moving straight after a turn.

8. **What real-world effects caused error or drift?**  
   Wheel friction and obstacles in the classroom were the main factors causing error or drift.

9. **What safety precautions did your team follow?**  
   We tested in a clear area, kept the emergency stop accessible, and safely raised the wheels during initial tests.

10. **If you had more time, how would you improve the controller?**  
    Since the controller is time-based, I would add motion feedback, such as odometry, to stop at measured distances and angles, then calibrate it using physical test results.
