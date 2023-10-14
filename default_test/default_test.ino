/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 https://www.arduino.cc/en/Tutorial/LibraryExamples/Sweep
*/

#include <Servo.h>

Servo myservo;  // base  rotstion
Servo servo1;   // base up down
Servo servo2;   // 35kg
Servo servo3;   //spider bot
Servo servo4;   //mg95
  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position



void setup()
{
  servo2.attach(11);
  servo1.attach(10);
  myservo.attach(9); 
  servo3.attach(8); 
  servo4.attach(6); 
  pinMode(7,OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  myservo.write(0);
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  for (pos = 0; pos <= 40; pos += 1) 
  { // goes from 0 degrees to 180 degrees
//    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(30);                       // waits 15 ms for the servo to reach the position
//  }
}

void Drop(){
  digitalWrite(7,HIGH);
  delay(2000);
  servo1.write(0);
  delay(3000);
    // attaches the servo on pin 9 to the servo object
  for (pos = 0; pos <= 80; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    servo2.write(pos);              // tell servo to go to position in variable 'pos'
    delay(30);                       // waits 15 ms for the servo to reach the position
  }
  delay(5000);
  for (pos = 40; pos >=0; pos -= 1) { // goes from 0 degrees to 180 degrees
//    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(30);                       // waits 15 ms for the servo to reach the position
//  }
   delay(3000);
  for (pos = 0; pos <= 10; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    servo1.write(pos);              // tell servo to go to position in variable 'pos'
    delay(30);                       // waits 15 ms for the servo to reach the position
  }
  digitalWrite(7,LOW);
  
}

void loop() {

  Drop();
  delay(100000);
}
//  for (pos = 0; pos <= 80; pos += 1) { // goes from 0 degrees to 180 degrees
//    // in steps of 1 degree
//    servo2.write(pos);              // tell servo to go to position in variable 'pos'
//    delay(30);                       // waits 15 ms for the servo to reach the position
//  }
//  delay(2000);
//  for (pos = 0; pos <= 30; pos += 1) { // goes from 0 degrees to 180 degrees
//    // in steps of 1 degree
//    servo1.write(pos);              // tell servo to go to position in variable 'pos'
//    delay(30);                       // waits 15 ms for the servo to reach the position
//  }

}
