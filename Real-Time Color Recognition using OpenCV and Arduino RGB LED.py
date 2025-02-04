import cv2 as cv  # Import the OpenCV library as cv
import numpy as np  # Import the NumPy library as np
import serial  # Import the serial library for serial communication
import time  # Import the time library for time-related functions

# Create a VideoCapture object to use the camera at index 1
cap = cv.VideoCapture(1)

# Start serial communication with Arduino on COM5 port
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=1)
time.sleep(2)  # Wait for 2 seconds to allow Arduino to initialize

# Function to determine the closest color based on HSV values
def closest_colour(h, s, v):
    # Loop through the defined color ranges
    for colour, (lower, upper) in colors_hsv.items():
        # Check if the pixel's hue, saturation, and value fall within the given range
        if lower[0] <= h <= upper[0] and lower[1] <= s <= upper[1] and lower[2] <= v <= upper[2]:
            return "red" if colour == "red2" else colour  # Merge red ranges
    return "undefined"  # Return "undefined" if no match is found

# Define color ranges in HSV format
colors_hsv = {
    "red": [(157, 149, 123), (180, 255, 255)],    # Lower red range
    "green": [(66, 57, 12), (95, 255, 255)],  # Green range
    "blue": [(91, 90, 0), (124, 175, 255)]   # Blue range
}

# Main loop to process video frames
while cap.isOpened():
    # Read a frame from the camera
    _, frame = cap.read()
    # Resize the frame to 800x600 pixels
    resized = cv.resize(frame, (800, 600))
    # Convert the resized frame from BGR to HSV color space
    hsv_frame = cv.cvtColor(resized, cv.COLOR_BGR2HSV)
    
    # Get the height and width of the HSV frame
    height = hsv_frame.shape[1]
    width = hsv_frame.shape[0]
    
    # Calculate the center pixel coordinates
    hh = height // 2
    ww = width // 2
    
    # Get the HSV values of the center pixel
    center_pixel = hsv_frame[ww, hh]
    
    # Extract hue, saturation, and value from the center pixel
    hue, sat, val = center_pixel[0], center_pixel[1], center_pixel[2]
    
    # Determine the closest color based on the HSV values
    colour = closest_colour(hue, sat, val)
    # Send the color to Arduino
    arduino.write(colour.encode())
    arduino.write(b'\n')  # Send a newline character for proper communication
    
    # If the color is defined, print it
    if colour != "undefined":
        print(colour)
    
    # Draw a circle at the center of the frame
    cv.circle(resized, (hh, ww), 5, (255, 255, 255), 3)
    
    # Display the resized frame in a window
    cv.imshow("Video Capture", resized)
    cv.waitKey(1)  # Wait for 1 millisecond for a key event
    
    # If 'q' is pressed, exit the loop
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()  # Close all OpenCV windows
        cap.release()  # Release the video capture object
        # Send 'off' signal to Arduino before closing
        arduino.write(b'off')
        # Close the serial communication
        arduino.close()