## Purpose of each library

[color library](/src/color.py) We are using the color library to determine which way the robot car will turn ither left or right and even slow down the car depending on the color.
[hc_sr04 library](/src/hc_sr04.py) It will be used for detecting the walls of the track. If the car is too close to the wall, it will turn left or right depending on which side the wall is being detected from.
[motors library](/src/motors.py) This is used for the robot car to move forward or backwards and if it has to stop, then it will stop moving.
[servo library](/src/servo.py) This library is used to turn the robot car left or right.
[timer library](/src/timer.py) It allows us to control time-related functions. We use it to time how long the servo should stay at a certain angle.
[main library](/src/main.py) This library combines all the libraries that we have, so all the functions have purpose for one another. For example, the color sensor will give a command to the motor and servo to do certain movements, and you can also combine the timer, so the motor is slowed down for a certain time and the servo will stay at a certain angle for a determined time.

## Crediting librarys
-[hc_sr04 library Roberto Sánchez](Apache License 2.0. https://www.apache.org/licenses/LICENSE-2.0")

This directory must contain code for control software which is used by the vehicle to participate in the competition and which was developed by the participants.

All artifacts required to resolve dependencies and build the project must be included in this directory as well.
