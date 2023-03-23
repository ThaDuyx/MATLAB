#include <Audio.h>
#include <Wire.h>
AudioInputI2S in;
AudioOutputI2S out;
AudioControlSGTL5000 audioShield;
AudioConnection patchCord0(in,0,out,0);
AudioConnection patchCord1(in,0,out,1);


void setup() {
  Serial.begin(9600);
  AudioMemory(6);
  audioShield.enable();
  audioShield.inputSelect(AUDIO_INPUT_MIC);
  audioShield.micGain(10); // in dB
  audioShield.volume(0.5);
}

void loop() {
  Serial.print("running");
  delay(1000);  // delay to avoid overloading the serial port buffer
}