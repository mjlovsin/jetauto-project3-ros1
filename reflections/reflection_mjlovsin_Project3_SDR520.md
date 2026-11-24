# MYLES LOVSIN-LABLANS 020150140
# Part I — Engineering reflection questions

Answer the following in your submission:

1. How did you establish communication with the robot?
    
    Connected through the robots WIFI VIA virtualbox ubuntu VM, Then SSH into it using ssh jetauto@192.168.149.1

2. Which velocity command topic did your robot use?

    Used /jetauto_controller/cmd_vel for movement commands.

3. How did you verify the message type expected by the robot?

    Used rostopic info /jetauto_controller/cmd_vel after running the motor controller. Which showed a twist message and the controller as the subcriber.

4. What final velocity and duration values did you use for each segment?

    1. Moving forward
        linear.x:  0.20 m/s
        linear.y:  0.00 m/s
        angular.z: 0.00 rad/s
        Duration:  6.00 s

    2. Moving left
        linear.x:  0.00 m/s
        linear.y:  0.20 m/s
        angular.z: 0.00 rad/s
        Duration:  6.00 s

    3. Rotating clockwise
        linear.x:  0.00 m/s
        linear.y:  0.00 m/s
        angular.z: -1.00 rad/s
        Duration:  1.55 s

    4. Moving right
        linear.x:  0.00 m/s
        linear.y: -0.20 m/s
        angular.z: 0.00 rad/s
        Duration:  6.00 s

    5. Rotating for arc
        linear.x:  0.00 m/s
        linear.y:  0.00 m/s
        angular.z: -1.00 rad/s
        Duration:  0.60 s

    6. Returning to start (combined forward motion and rotation)
        linear.x:  0.20 m/s
        linear.y:  0.00 m/s
        angular.z: 0.20 rad/s
        Duration:  6.75 s

    7. Turning back to normal
        linear.x:  0.00 m/s
        linear.y:  0.00 m/s
        angular.z: 1.00 rad/s
        Duration:  1.25 s
   
5. How close was the robot to the intended 1-meter motion segments?

    Pretty close followed the square rotation required enough for professor to accept it. We did not pull out a measuring tape, but by eyeball ballpark it as being aroudn the correct measurement.

6. How did Gazebo or simulation timing differ from physical robot timing, if you tested both?

    Had to reduce clockwise turning as it was over turning and wasnt lining up, dropped it from 1.76 to 1.55 could probably drop it to 1.4 or so but proff OK that it was close enough.

7. Which motion segment was hardest to tune: forward, lateral, turn, or combined motion? Why?

    The arc forsure, had to constantly adjust its time, the inital angle for it, then the constant turning radius afterwards, then i also had to eyeball adjust it back to square for the reset.


8. What real-world effects caused error or drift?

    ground being slippery, or uneven would do so, our ground in the school is poured concreate so i would say its probably the best surface we could of found to demonstrate.


9. What safety precautions did your team follow?

    We made sure no one was around to trip over the robot, we made sure that we were ready to pick it up if it started driving into something, we cleared the area where we perceieved it would go before starting it best we could.

10. If you had more time, how would you improve the controller?

    Would fix it to being completely square after finishing, we were pretty spot on with the location it ended at but the rotation was off, 
