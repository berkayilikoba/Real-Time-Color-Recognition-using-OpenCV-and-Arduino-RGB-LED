# Real-Time Color Recognition using OpenCV and Arduino RGB LED

## Overview
This project utilizes OpenCV to capture live video and determine the HSV color of the center pixel. The detected color is then converted to RGB and transmitted to an Arduino, which controls an RGB LED to match the identified color in real time.

## Features
- Real-time color detection using OpenCV
- HSV to RGB conversion for accurate color representation
- Serial communication between OpenCV (Python) and Arduino
- Dynamic RGB LED color control

## Requirements
### Hardware
- Arduino (Uno, Mega, or compatible)
- RGB LED (Common Anode or Cathode)
- Resistors (appropriate for the LED)
- USB cable for Arduino
- Camera (built-in or external webcam)

### Software
- Python 3.x
- OpenCV
- NumPy
- PySerial
- Arduino IDE

## Installation & Setup

### 1. Install Python Dependencies
Ensure you have Python installed, then install the required libraries:
```bash
pip install opencv-python numpy pyserial
```

### 2. Upload Arduino Code
1. Open the Arduino IDE.
2. Upload the provided Arduino sketch (`arduino_led_control.ino`) to your board.

### 3. Run the Python Script
Execute the Python script to start detecting colors and controlling the RGB LED:
```bash
python color_detection.py
```

## How It Works
1. OpenCV captures frames from the camera.
2. The HSV color of the center pixel is analyzed.
3. The HSV value is converted to an RGB format.
4. The RGB values are sent to the Arduino via serial communication.
5. The Arduino adjusts the RGB LED accordingly.

## Usage
- Place an object with a distinct color in front of the camera.
- The RGB LED should change to match the detected color.
- Adjust lighting and camera positioning for better accuracy.

## Example Output
- If the detected color is red, the RGB LED glows red.
- If the detected color is blue, the RGB LED glows blue.

## Future Improvements
- Implement support for multiple LEDs.
- Improve color accuracy with adaptive thresholding.
- Add GUI for user interaction.

## License
This project is open-source and available under the MIT License.

## Youtube Videos
How to use optimizer.py: https://www.youtube.com/watch?v=BJxyvGwTRsk
Project: https://www.youtube.com/watch?v=6UfTzsqHOSs
