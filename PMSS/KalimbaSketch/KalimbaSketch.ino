#include <Bounce.h>  // Bounce library makes button change detection easy
/// --- MIDI 
const int channel = 1;

/// --- PIEZO 
const int knockSensor = A0;                 // the piezo is connected to analog pin 0
const int threshold = 500;                  // threshold value to decide when the detected sound is a knock or not
int sensorReading = 0;                      // variable to store the value read from the sensor pin

/// --- BUTTON
const int buttonPin = 0;                    // the number of the pushbutton pin
int buttonState = 0;                        // variable for reading the pushbutton status

/// --- STATE
bool isPlaying = false;                     // note triggered


/// --- Setup
void setup() {
  Serial.begin(9600);                       // use the serial port
  pinMode(buttonPin, INPUT);
}


/// --- Runtime
void loop() {
  sensorReading = analogRead(knockSensor);  // read the sensor and store it in the variable sensorReading:
  buttonState = digitalRead(buttonPin);

  if (sensorReading >= threshold) {
    usbMIDI.sendNoteOn(60, 99, channel);    // MIDI 60 = C4 Note
    Serial.println("Knock!");
    isPlaying = true;
    delay(500);
  }

  if (isPlaying) {
    usbMIDI.sendNoteOff(60, 99, channel);   
    isPlaying = false;
  }
  
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    Serial.print("ON");
  } else {
    Serial.print("OFF");
  }

  delay(500);
}
