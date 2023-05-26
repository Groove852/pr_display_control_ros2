#!/usr/bin/env python3
# Importing necessary libraries
import customtkinter as ctk
import tkinter as tk
import datetime
import psutil
 
# Sets the appearance of the window
# Supported modes : Light, Dark, System
# "System" sets the appearance mode to
# the appearance mode of the system
ctk.set_appearance_mode("System")  
 
# Sets the color of the widgets in the window
# Supported themes : green, dark-blue, blue   
ctk.set_default_color_theme("dark-blue")   
 
appWidth, appHeight = 1024, 600
 

# Define the App class for displaying the app
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        # Set up title for display
        self.title("Nyanya dispaly")  
        
        # Set up variables for updating on display
        self.time = "time_info"
        self.power = "power_output"
        
        self.geometry(f"{appWidth}x{appHeight}") 
        # self.attributes("-fullscreen", True)

        self.grid_rowconfigure((0,1), weight=0)
        
        self.state = None
        # Create the system info frame
        self.system_info_frame = ctk.CTkFrame(master=self,
                                              width=985,
                                              corner_radius=10)
        self.system_info_frame.grid(row=0,
                                    column=0,
                                    rowspan=4,
                                    padx=(20, 20),
                                    pady=(20, 0),
                                    sticky="nsew")
        
        # Create the status info frame for display status
        self.status_info_frame = ctk.CTkFrame(master=self,
                                              width=985, 
                                              height=340, 
                                              corner_radius=10)
        self.status_info_frame.grid(row=4, 
                                    column=0, 
                                    rowspan=8, 
                                    padx=(20, 20), 
                                    pady=(20, 0), 
                                    sticky="nsew")
        
        # Configure the grid layout for the status info frame
        self.status_info_frame.grid_columnconfigure((0, 1), weight=1)
        self.status_info_frame.grid_rowconfigure((0, 1), weight=1)
        
        # Configure the grid layout for the system info frame
        self.system_info_frame.grid_columnconfigure((0, 2), weight=1)
        self.system_info_frame.grid_columnconfigure(1, weight=0)
        
        # Set up variables for temperature and CPU progress bars
        self.temperature = tk.Variable(master=self.system_info_frame, value=0.0)
        self.cpu = tk.Variable(master=self.system_info_frame, value=(psutil.cpu_percent() / 100))
        
        # Create scatic labels for system info
        self.time_label = ctk.CTkLabel(master=self.system_info_frame,
                                       text="Time: ",
                                       anchor="w",
                                       font=ctk.CTkFont(size=14))
        self.power_label = ctk.CTkLabel(master=self.system_info_frame,
                                        text="Power: ",
                                        anchor="w",
                                        font=ctk.CTkFont(size=14))
        self.cpu_label = ctk.CTkLabel(master=self.system_info_frame,
                                    text="CPU: ",
                                    anchor="w",
                                    font=ctk.CTkFont(size=14))
        self.temperature_label = ctk.CTkLabel(master=self.system_info_frame,
                                              text="Temperature: ",
                                              anchor="w",
                                              font=ctk.CTkFont(size=14))
        
        # Create output labels for system info frame
        self.time_info = ctk.CTkLabel(master=self.system_info_frame,
                                      text=self.time,
                                      anchor="w")
        self.power_info = ctk.CTkLabel(master=self.system_info_frame,
                                       text=self.power,
                                       anchor="w")
        
        # Create progress bar for system info frame
        self.cpu_progress = ctk.CTkProgressBar(master=self.system_info_frame,
                                               width=500,
                                               variable=self.cpu)
        self.temperature_progress = ctk.CTkProgressBar(master=self.system_info_frame,
                                                       width=500,
                                                       variable=self.temperature)
        
        # Set the grid layout for the static labels
        self.time_label.grid(row=0, column=0, padx=10, pady=(10, 10))
        self.power_label.grid(row=1, column=0, padx=10, pady=(10, 10))
        self.cpu_label.grid(row=2, column=0, padx=10, pady=(10, 0))
        self.temperature_label.grid(row=3, column=0, padx=10, pady=(0, 10))
        
        # Set the grid layout for the output labels
        self.time_info.grid(row=0, column=1, padx=10, pady=(10, 10))
        self.power_info.grid(row=1, column=1, padx=10, pady=(10, 10))
        
        # Set the grid layout for the progress bar
        self.cpu_progress.grid(row=2, column=1, padx=10, pady=(13, 2), sticky="ew")
        self.temperature_progress.grid(row=3, column=1, padx=10, pady=(2, 13), sticky="ew")
        
        # Set the label and text box layout for the status bar
        self.status_label = ctk.CTkLabel(master=self.status_info_frame,
                                         text="STATUS",
                                         anchor="w",
                                         font=ctk.CTkFont(size=16))
        self.status_info = ctk.CTkTextbox(self.status_info_frame, 
                                          width=200, 
                                          height=290,
                                          corner_radius=10)
        
        # Set the grid layout for the labels and text box
        self.status_label.grid(row=0, column=0, padx=460, pady=(20, 10))
        self.status_info.grid(row=1, column=0, rowspan=3, padx=(20, 20), pady=(10, 20), sticky="nsew")
        
        self.status_info.insert("0.0", "[STATUS] " + "OK" + "\n")
        
        # Bind the 'F11' and 'Escape' keys for fullscreen mode
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.end_fullscreen)
    
    # Define functions for toggling and ending fullscreen mode
    def toggle_fullscreen(self, event=None):
        """Toggles the fullscreen mode of the application window.

        :param event: Pressing a preset button to perform a function.
        :type event: tkinter.Event
        :rtype: str
        """
        self.state = not self.state
        self.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        """Closes the application window.

        :param event: Pressing a preset button to perform a function.
        :type event: tkinter.Event
        :rtype: str
        """
        self.destroy()
        return "break"
    
    # Define functions for updating the CPU, temperature, power, time, and status
    def update_cpu(self, value=None):    
        """Updates the CPU progress bar with the current CPU usage.

        :param value: The transferred value is only necessary for asynchronous operation of the function via ROS
        """
        self.cpu_progress.configure(variable=tk.Variable(self.system_info_frame, float(psutil.cpu_percent / 100)))
        self.cpu_progress.update()
        
    def update_time(self, value=None):
        """Updates the time information with the current time.

        :param value: The transferred value is only necessary for asynchronous operation of the function via ROS
        """
        self.time_info.configure(text=str(datetime.datetime.now().strftime("%H:%M:%S")))
        self.time_info.update()
        
    def update_temperature(self, value=None):
        """Updates the temperature progress bar with the current temperature value.

        :param value: Value of the current temperature to output to the application
        :type value: std_msgs.msg.Float32
        """
        self.temperature_progress.configure(variable=tk.Variable(self.system_info_frame, float(value.temperature.data / 100)))
        self.temperature_progress.update()    
        
    def update_power(self, value=None):
        """Updates the power information with the current voltage value.

        :param value: Value of the current power to output to the application
        :type value: std_msgs.msg.Float32
        """
        self.power_info.configure(text=str(value.voltage.data) + "V")
        self.power_info.update()
        
    def update_status(self, value=None):
        """Updates the status information with a new message.

        :param value: Data about the current system state or information about the error that occurred
        :type value: std_msgs.msg.String
        """
        self.status_info.delete("0.0", "1000.0")
        self.status_info.insert(f"0.0", "[STATUS] " + value.data+ "\n")
        self.status_info.update()
        
        
# Define the main function for the app and run it
def main():
    app = App()
    app.mainloop()

# Call the main function
if __name__ == "__main__":
    main()