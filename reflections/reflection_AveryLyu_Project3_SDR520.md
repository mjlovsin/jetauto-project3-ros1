# Project 3 — Reflection

**Name:** Avery Lyu
**Stu#:** 183244235
**Course:** SDR520

---

## Final parameters and calibration table

These values are the final parameters used on the real JetAuto. The commanded result is velocity multiplied by duration.

| Motion | Velocity command | Duration | Commanded result |
|---|---|---:|---|
| Forward | `linear.x = 0.2` m/s | 6.00 s | 1.2 m |
| Left sideways | `linear.y = +0.2` m/s | 6.00 s | 1.2 m |
| Clockwise turn | `angular.z = -1.0` rad/s | 1.55 s | 1.55 rad (about 88.8°) |
| Right sideways | `linear.y = -0.2` m/s | 6.00 s | 1.2 m |
| Arc rotation | `angular.z = -1.0` rad/s | 0.60 s | 0.6 rad (about 34°) |
| Forward + turn (return) | `linear.x = 0.2`, `angular.z = +0.2` | 6.75 s | Arc with radius 1 m, about 1.35 rad (about 77°) |
| Turn back to starting heading | `angular.z = +1.0` rad/s | 1.25 s | 1.25 rad (about 71.6°) |

**Adjustments:** The clockwise turn was reduced from 1.76 s (simulation) to 1.55 s on the real robot. The longer time over-turned and the path no longer looked square. It could probably go down to about 1.4 s.

**Observation:** The robot traced a recognizable square and finished close to the intended position, but its final heading was slightly off, so the motion was not perfectly repeatable between runs. Distances were judged by eye and not measured with a tape.

---

## Reflection answers

**1. How did you establish communication with the robot?**
We connected to the JetAuto's Wi-Fi network and used SSH (`ssh jetauto@192.168.149.1`) to log in to the robot. We launched the hardware controller with `roslaunch jetauto_controller jetauto_controller.launch` and ran our control script on the robot, so the ROS master and the script were on the same machine.

**2. Which velocity command topic did your robot use?**
`/jetauto_controller/cmd_vel`, not the generic `/cmd_vel`.

**3. How did you verify the message type expected by the robot?**
We ran `rostopic info /jetauto_controller/cmd_vel` after starting the motor controller. It reported `geometry_msgs/Twist` as the message type and listed the controller as the subscriber. This confirmed the message type and that the hardware controller was listening before we ran any motion code.

**4. What final velocity and duration values did you use for each segment?**
See the calibration table above. Forward, left, and right each used 0.2 m/s for 6.0 s. The clockwise turn used -1.0 rad/s for 1.55 s. The arc rotation used -1.0 rad/s for 0.6 s. The combined return used 0.2 m/s forward with +0.2 rad/s for 6.75 s. The final turn back used +1.0 rad/s for 1.25 s.

**5. How close was the robot to the intended 1-meter motion segments?**
We did not measure with a tape measure. By visual estimate, each segment was roughly 1 m, and the instructor accepted the square as close enough. Commanded distance is velocity times time, so 0.2 m/s for 6 s is 1.2 m on paper. The actual distance depends on wheel slip and acceleration, which we did not measure.

**6. How did Gazebo or simulation timing differ from physical robot timing?**
The clockwise turn needed 1.76 s in simulation, but on the real robot it over-turned and the path no longer looked square, so we reduced it to 1.55 s. The simulator applies commanded velocity almost exactly, while the real robot accelerates gradually and is affected by floor friction. The physical timings therefore had to be tuned by observation.

**7. Which motion segment was hardest to tune, and why?**
The arc (combined forward and turn return) was the hardest. We adjusted its duration, the initial rotation before it, and the constant turning radius it follows. Because it is a curved path, it is harder to judge by eye than a straight segment, and errors from the earlier segments carry into it. After the arc we also had to adjust by eye to bring the robot back to square for the reset.

The final path is a curve rather than a straight line. This is expected: the combined command (`linear.x = 0.2` with `angular.z = +0.2`) makes the robot follow a constant-radius arc of R = v / ω = 0.2 / 0.2 = 1 m. The project brief allows either this advanced turning motion or a simpler forward-then-turn return. We chose the arc, so the small curve back toward the start is the intended behavior and not a bug. Wheel slip explains the rest of the difference from the ideal path.

**8. What real-world effects caused error or drift?**
Floor friction was the main factor. Slippery or uneven ground lets the wheels slip. Our school floor is poured concrete, which is probably one of the best surfaces available for this demonstration, so the error would likely be larger on other floors. Other likely contributors include battery level and the robot not reaching commanded speed instantly. We did not isolate these factors. Because the controller is open-loop, nothing corrects position or heading during a run, so errors accumulate across segments and repetitions.

**9. What safety precautions did your team follow?**
- We cleared the area the robot would travel through and made sure no one was nearby who could trip over it.
- One teammate stayed ready to pick the robot up if it started driving toward something.
- The emergency stop was accessible during all tests.
- Only one motion controller ran at a time, so commands could not conflict.
- We sent a zero-velocity stop command between segments.

**10. If you had more time, how would you improve the controller?**
The main improvement would be making the robot finish fully square. It ended very close to the intended position, but its final rotation was off. Adding odometry or encoder feedback would let each segment end based on measured distance or angle instead of fixed time. Moving the tuned values into ROS parameters or a YAML file would make retuning easier without editing code. A start countdown and a safety timeout would also be useful, along with logging each executed segment and measuring real end poses against floor markers.

---

## GenAI declaration

I used an AI coding assistant (Cursor) for guidance on the Project 3 controller structure, ROS command debugging. I ran and tested the motion sequence on the real JetAuto robot myself, and I calibrated the final parameters based on observed motion.
