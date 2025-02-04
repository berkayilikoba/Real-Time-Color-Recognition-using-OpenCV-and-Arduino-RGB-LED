import cv2 as cv  # Import the OpenCV library as cv
import numpy as np  # Import the NumPy library as np

# Open the camera
cap = cv.VideoCapture(1)

# Define a dummy function for trackbar callback
def nothing(x):
    pass  # This function does nothing, it's just a placeholder

# Create a window for the trackbars
cv.namedWindow('Trackbars')

# Set initial values for Hue, Saturation, and Value trackbars
cv.createTrackbar('Hue Min', 'Trackbars', 0, 180, nothing)  # Minimum Hue
cv.createTrackbar('Hue Max', 'Trackbars', 180, 180, nothing)  # Maximum Hue
cv.createTrackbar('Saturation Min', 'Trackbars', 0, 255, nothing)  # Minimum Saturation
cv.createTrackbar('Saturation Max', 'Trackbars', 255, 255, nothing)  # Maximum Saturation
cv.createTrackbar('Value Min', 'Trackbars', 0, 255, nothing)  # Minimum Value
cv.createTrackbar('Value Max', 'Trackbars', 255, 255, nothing)  # Maximum Value

# Main loop to process video frames
while True:
    ret, frame = cap.read()  # Read a frame from the camera
    if not ret:  # If the frame was not captured successfully, exit the loop
        break

    # Convert the captured frame from BGR to HSV color space
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Get the HSV boundaries from the trackbars
    h_min = cv.getTrackbarPos('Hue Min', 'Trackbars')  # Minimum Hue value
    h_max = cv.getTrackbarPos('Hue Max', 'Trackbars')  # Maximum Hue value
    s_min = cv.getTrackbarPos('Saturation Min', 'Trackbars')  # Minimum Saturation value
    s_max = cv.getTrackbarPos('Saturation Max', 'Trackbars')  # Maximum Saturation value
    v_min = cv.getTrackbarPos('Value Min', 'Trackbars')  # Minimum Value
    v_max = cv.getTrackbarPos('Value Max', 'Trackbars')  # Maximum Value

    # Create a mask based on the HSV boundaries
    lower_bound = np.array([h_min, s_min, v_min])  # Lower bound for the mask
    upper_bound = np.array([h_max, s_max, v_max])  # Upper bound for the mask
    mask = cv.inRange(hsv, lower_bound, upper_bound)  # Create the mask

    # Apply the mask to show only the regions of the target color
    result = cv.bitwise_and(frame, frame, mask=mask)  # Bitwise AND operation to isolate the color

    # Display the result
    cv.imshow("Result", result)  # Show the masked result

    # Exit the loop if 'q' key is pressed
    if cv.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()  # Release the camera
cv.destroyAllWindows()  # Close all OpenCV windows