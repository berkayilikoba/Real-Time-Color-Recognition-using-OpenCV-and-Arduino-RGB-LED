// Define the pin numbers for RGB LED
#define r_led 4
#define g_led 3
#define b_led 5

void setup() {
  // Start serial communication at 9600 baud rate
  Serial.begin(9600);

  // Set LED pins as OUTPUT
  pinMode(r_led, OUTPUT);  // Red LED pin as output
  pinMode(g_led, OUTPUT);  // Green LED pin as output
  pinMode(b_led, OUTPUT);  // Blue LED pin as output
}

void loop() {
  // Check if data is available to read from serial input
  if (Serial.available() > 0) {
    // Read the incoming message as a string
    String message = Serial.readString();

    // Check the message and control the LEDs accordingly
    if (message.equals("red")) {
      // Turn on the red LED and turn off the others
      digitalWrite(r_led, HIGH);
      digitalWrite(g_led, LOW);
      digitalWrite(b_led, LOW);
    }
    else if (message.equals("green")) {
      // Turn on the green LED and turn off the others
      digitalWrite(r_led, LOW);
      digitalWrite(g_led, HIGH);
      digitalWrite(b_led, LOW);
    }
    else if (message.equals("blue")) {
      // Turn on the blue LED and turn off the others
      digitalWrite(r_led, LOW);
      digitalWrite(g_led, LOW);
      digitalWrite(b_led, HIGH);
    }
    else {
      // If the message is not recognized, turn off all LEDs
      digitalWrite(r_led, LOW);
      digitalWrite(g_led, LOW);
      digitalWrite(b_led, LOW);
    }
  }
  
}