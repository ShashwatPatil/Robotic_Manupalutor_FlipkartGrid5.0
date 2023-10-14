

#include <Servo.h>

int inbyte = '0';

Servo myservo;  // base  rotstion
Servo servo1;   // base up down
Servo servo2;   // 35kg
Servo servo3;   //spider bot
Servo servo4;   //mg95

int servo0pos = 0;
int servo1pos = 0;
int servo2pos = 0;
int servo3pos = 0;
int servo4pos = 0;
 
// create servo object to control a servo
// twelve servo objects can be created on most boards
// variable to store the servo position

void setup() {
  Serial.begin(9600);
  servo2.attach(11);
  servo1.attach(10);
  myservo.attach(9); 
  servo3.attach(8); 
  servo4.attach(6); 
  pinMode(7,OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  myservo.write(0);
  servo1.write(0);
  servo2.write(90);
  servo3.write(0);
  servo4.write(0);
  // attaches the servo on pin 9 to the servo object
}

void loop() {
  if(Serial.available()>0){
    inbyte = Serial.read();
    
    
    if(inbyte == 'a'){
      servo1pos = servo1pos + 1;
      servo1.write(servo1pos);
      
    }
    if(inbyte == 'b'){
      servo1pos = servo1pos - 1;
      servo1.write(servo1pos);
    }
    if(inbyte == 'c'){
      servo0pos = servo0pos + 1;
      myservo.write(servo0pos);
    }
    if(inbyte == 'd'){
      servo0pos = servo0pos - 1;
      myservo.write(servo0pos);      
    }
    if(inbyte == 'e'){
      digitalWrite(7,LOW);
      
    }
    if(inbyte == 'f'){
      digitalWrite(7,HIGH);
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
        delay(100);                       // wait for a second
        digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
        delay(100);
      
    }
    if(inbyte == 'g'){
      servo0pos = 0;
      servo1pos = 0;
      servo2pos = 90;
      servo3pos = 0;
      servo4pos = 0;
      servo4.write(0);
      delay(400);
      servo3.write(0);
      delay(400);
      servo2.write(90);
      delay(200);
      servo1.write(0);
      delay(200);
      myservo.write(0);

    }
    if(inbyte == 'h'){
      servo2pos = servo2pos - 1;
      servo2.write(servo2pos);
    }
    if(inbyte == 'i'){
      servo2pos = servo2pos + 1;
      servo2.write(servo2pos);
    }
    if(inbyte == 'j'){
      
      
    }
    if(inbyte == 'k'){
      servo3pos = servo3pos - 1;
      servo3.write(servo3pos);
    }
    if(inbyte == 'l'){
      servo3pos = servo3pos + 1;
      servo3.write(servo3pos);
    }
    if(inbyte == 'm'){
      servo4pos = servo4pos + 5;
      servo4.write(servo4pos);
    }
    if(inbyte == 'n'){
      servo4pos = servo4pos - 5;
      servo4.write(servo4pos);
    }
    if(inbyte == 'o'){
      
    }
    if(inbyte == 'p'){
      
    }
  }

}
