#include <Bounce.h>  // Bounce library makes button change detection easy

const int knockSensor = A0; // the piezo is connected to analog pin 0
const int threshold = 500;  // threshold value to decide when the detected sound is a knock or not
const int channel = 1;

// these variables will change:
int sensorReading = 0;      // variable to store the value read from the sensor pin
bool isPlaying = false;

void setup() {
  Serial.begin(9600);       // use the serial port
}

void loop() {
  // read the sensor and store it in the variable sensorReading:
  sensorReading = analogRead(knockSensor);

  if (sensorReading >= threshold) {
    usbMIDI.sendNoteOn(60, 99, channel);  // 60 = C4
    Serial.println("Knock!");
    isPlaying = true;
    delay(500);
  }

  if (isPlaying) {
    usbMIDI.sendNoteOff(60, 99, channel);  // 60 = C4
    isPlaying = false;
  }
  
}
