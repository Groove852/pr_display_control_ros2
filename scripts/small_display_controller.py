#!/usr/bin/env python3
# Importing necessary libraries
import cv2
import screeninfo


# Defining a SmallDisplayController class to display the image
class SmallDisplayController(object):
    """
    Display controller class, designed to control images and text on screen using OpenCV 
    """
    def __init__(self, window_name = "test", screen_id = 0,  *args, **kwargs):
        """ 
        Controller for small display on the nyanya
        
        :param window_name: The name of the application to output the image
        :param screen_id: Monitor ID on which the value will be displayed
        """
        # Get the screen info from the screen_id parameter to define where to display the window
        self.screen = screeninfo.get_monitors()[screen_id]
        # Define the window name
        self.window_name = window_name
    
    # Function to show an image on the screen
    def show_image(self, path):
        """Function that displays an image at the specified path.
        It shows the image on the specified screen and waits for the user to close the window before exiting.

        :param path: The path and file name of the image to show.
        :type path: str
        """
        # Load the image from the path
        image = cv2.imread(path)
        
        # Set the window up to be full-screen
        cv2.namedWindow(self.window_name, cv2.WND_PROP_FULLSCREEN)
        cv2.moveWindow(self.window_name, self.screen.x - 1, self.screen.y - 1)
        cv2.setWindowProperty(self.window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        # Show the image on the window and wait for the user to close the window
        cv2.imshow(self.window_name, image)
        cv2.waitKey()
        
        # Close the window to free resources
        cv2.destroyAllWindows()
        
        
# Defining a main function
def main():
    # Define the screen ID to be used
    screen_id = 0
    
    # Set the path to the image to be displayed
    path = r'/home/neq/ws/applied_ws/src/pr_display_control_ros2/images/green.png'

    # Create a SmallDisplayController object and show the image on the specified screen
    display = SmallDisplayController("small_screen", screen_id)
    display.show_image(path)

# Call the main function
if __name__ == '__main__':
    main()