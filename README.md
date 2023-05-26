# pr_display_control_ros2

This repository contains three codes for controlling display on the robot's screen, along with an app_controller GUI that displays system state data on the humanoid robot's main display.

- **app_controller:** This is a graphical user interface designed to display real-time system state data on the robot's main display. It allows the user to monitor various parameters and settings in the system.

- **big_display_controller:** This code connects to the ROS2 topics used by the app_controller, extracts data and layout information, and sends it to the robot's main display.

- **small_display_controller:** This code controls a secondary display on the robot, displaying images and text. It offers functions for showing images and overlaying text.

## Demo

![Demo](demo.png)

## Requirements

This code requires Python3, along with the following Python packages:
- ROS2
- screeninfo
- Tkinter
- customtkinter
- OpenCV

#### To install the dependencies:

pip3 install screeninfo opencv-python


## Usage

- Open three terminals and navigate to the path /pr_display_control_ros2/src/
- In one terminal:

ros2 run pr_display_control_ros2 big_display_controller

- In the second terminal:

ros2 run pr_display_control_ros2 small_display_controller.py


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
