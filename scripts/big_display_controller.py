#!/usr/bin/env python3
# Importing necessary libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32

# Importing custom module app_controller for controlling the app
import app_controller


# Defining a BigDisplayController class that inherits from the Node class
class BigDisplayController(Node):    
    """
    A class that represents a ROS node to control a GUI for displaying robot status (temperature, power, and CPU usage).
    """
    def __init__(self, *args, **kwargs):
        """ 
        Controller for the display on the nyanya
        
        It initializes the ROS node, creates an instance of the App class
        (from the app_controller module) to control the GUI,
        and subscribes to several topics to receive robot status data. 
        """
        # Calling the initialization function of the Node class with a name for the node
        super().__init__('big_display_app')
        
        # Creating an instance of the App class from app_controller module
        self.app = app_controller.App()
        
        # Creating subscribers for different topics with a set QoS profile for each
        self.power_subscriber = self.create_subscription(msg_type=Float32,
                                                        topic="power",
                                                        callback=self.app.update_power,
                                                        qos_profile=10)
        self.temperature_subscriber = self.create_subscription(msg_type=Float32,
                                                        topic="temperature",
                                                        callback=self.app.update_temperature,
                                                        qos_profile=10)
        self.time_subscriber = self.create_subscription(msg_type=Float32,
                                                        topic="power",
                                                        callback=self.app.update_time,
                                                        qos_profile=10)
        self.cpu_subscriber = self.create_subscription(msg_type=Float32,
                                                        topic="power",
                                                        callback=self.app.update_cpu,
                                                        qos_profile=10)
        self.status_subscriber = self.create_subscription(msg_type=String,
                                                        topic="Status",
                                                        callback=self.app.update_status,
                                                            qos_profile=10)
    
    # Defining a run method to keep the program running via rclpy continous spinning
    def run(self):
        """A function that is responsible for continually spinning the ROS node to receive updates from subscribed topics."""
        try:
            while rclpy.ok():
                rclpy.spin_once(self)
                print("ok")
        except:
            self.destroy_node()
            rclpy.shutdown()
            
# Defining a main function
def main():
    # Initializing rclpy library
    rclpy.init()
    # Creating an instance of the BigDisplayController class
    display = BigDisplayController()
    # Calling the run method via app.after method which allows the window to close properly after closing
    display.app.after(500, display.run, 30)
    # Running the tkinter mainloop to start the GUI program
    display.app.mainloop()

# Running the main function only if the module is being run directly
if __name__ == '__main__':
    main()
    
    
    
    