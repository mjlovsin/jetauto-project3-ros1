# Project 3: Real-World JetAuto Motion Control Reflection

**Name:** Cynthia Salazar  
**Course:** SDR520

## Final parameters and calibration table

These are the final values used by the group on the real JetAuto. The commanded result is velocity multiplied by duration, rather than a measurement of the robot’s actual movement.

| Motion | Velocity command | Final duration | Commanded result |
|---|---|---:|---|
| Forward | `linear.x = 0.2` m/s | 6.00 s | 1.2 m |
| Left sideways | `linear.y = +0.2` m/s | 6.00 s | 1.2 m |
| Clockwise turn | `angular.z = -1.0` rad/s | 1.55 s | 1.55 rad (about 88.8° clockwise) |
| Right sideways | `linear.y = -0.2` m/s | 6.00 s | 1.2 m |
| Rotation before the arc | `angular.z = -1.0` rad/s | 0.60 s | 0.6 rad (about 34.4° clockwise) |
| Forward + turn (return) | `linear.x = 0.2` m/s, `angular.z = +0.2` rad/s | 6.75 s | 1.35 m along an arc, 1.35 rad (about 77.3° counterclockwise) |
| Turn back to starting heading | `angular.z = +1.0` rad/s | 1.25 s | 1.25 rad (about 71.6° counterclockwise) |

**Adjustment:** The clockwise turn was reduced from 1.76 seconds in simulation to 1.55 seconds on the real robot because the longer duration made it turn too far.

**Observation:** The robot traced a recognizable square and finished close to the intended position, but its final heading was slightly off. Distances were estimated by eye rather than measured with a tape measure.

## Reflection answers

**1. How did you establish communication with the robot?**

We connected to the robot’s Wi-Fi network and opened an SSH session using `ssh jetauto@192.168.149.1`. Once connected, we sourced the ROS environment and started the hardware controller with `roslaunch jetauto_controller jetauto_controller.launch`. We then ran the motion script on the robot through SSH.

**2. Which velocity command topic did your robot use?**

The robot used `/jetauto_controller/cmd_vel`. This was the topic the code published to when sending movement commands.

**3. How did you verify the message type expected by the robot?**

The team checked it using `rostopic info /jetauto_controller/cmd_vel`. The output showed `geometry_msgs/Twist` and listed the hardware controller as a subscriber. This confirmed both the message type and that the controller was listening before testing movement.

**4. What final velocity and duration values did you use for each segment?**

The final values are listed in the shared calibration table. Forward, left, and right movement each used 0.2 m/s for 6 seconds. The clockwise turn used −1.0 rad/s for 1.55 seconds, followed later by another clockwise rotation at the same speed for 0.6 seconds before the arc. The combined forward-and-turn movement used 0.2 m/s forward and +0.2 rad/s for 6.75 seconds. Finally, the robot turned at +1.0 rad/s for 1.25 seconds to bring its heading closer to the starting direction.

**5. How close was the robot to the intended 1-meter motion segments?**

The segments looked close to the intended length, but the team did not use a tape measure, so there was no exact measurement. The robot made a recognizable square and finished close to the intended position, although its final heading was slightly off. One thing I learned was that the commanded distance and actual distance are different: 0.2 m/s for 6 seconds gives 1.2 meters on paper, but that does not tell me exactly how far the robot moved.

**6. How did Gazebo or simulation timing differ from physical robot timing, if you tested both?**

The team initially used 1.76 seconds for the clockwise turn in simulation. On the real robot, that made it turn too far, so the time was reduced to 1.55 seconds. This showed me why simulation timings cannot just be carried over without testing. The physical robot’s response and contact with the floor affect the movement, so the values needed adjustment.

**7. Which motion segment was hardest to tune: forward, lateral, turn, or combined motion? Why?**

The combined forward-and-turn movement was the hardest part for me to figure out while helping with the code. For a straight movement, it was easier to think about the direction and duration separately. With the arc, changing the duration affected both the robot’s position and its heading. Errors from earlier movements also carried into that segment, so getting it to return close to the start took more adjustment.

**8. What real-world effects caused error or drift?**

Wheel slip and floor friction could make the robot move differently from the programmed path. Acceleration and stopping also matter because the robot does not instantly reach or leave the commanded speed. Battery level was another possible factor, although the team did not test these causes separately. Since the controller was time-based, it had no position feedback to notice an error and correct it during the run.

**9. What safety precautions did your team follow?**

The team kept the robot’s path clear of people and obstacles. One teammate also stayed close and watched the robot throughout testing to help prevent collisions or damage, ready to stop it if it moved unexpectedly. The emergency stop command was kept accessible during testing so there was a way to stop the robot without waiting for the sequence to finish. Only one movement controller ran at a time to avoid conflicting commands. The script also sent a zero-velocity command between segments and at the end of the sequence. This project helped me understand that checking how to stop the robot is just as important as getting it to move, especially when testing a path that still needs calibration.

**10. If you had more time, how would you improve the controller?**

I would start by using floor markers to measure the distance travelled and the final heading after each segment, then record the results over several runs. That would help me see whether an error was consistent or changed between attempts, instead of adjusting the timing based only on how the path looked. My next improvement would be to use odometry feedback so the controller could check the robot’s estimated position and heading and correct its movement, rather than depending only on fixed durations. Odometry can still be affected by wheel slip, so I would compare its readings with the floor measurements. I would also add a start countdown to give everyone time to step back and a safety timeout to stop movement if a segment ran longer than expected. My main goal would be to improve the final heading and make both repetitions follow a more consistent path.

## GenAI declaration

I used Claude Code and Codex for guidance on the project setup, motion-control code, and troubleshooting. I ran and tested the square-motion sequence on the physical robot with my team and helped fine-tune the final parameters based on its observed movement.
