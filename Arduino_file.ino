#include <Servo.h>

Servo myservo;

int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo.write(0);
}

void loop() {
  if (Serial.available() > 0){
    String msg = Serial.readString();

    if (msg == "TOKEN"){
      myservo.write(60);
      delay(1000);
      myservo.write(0);
    }
  }

}
