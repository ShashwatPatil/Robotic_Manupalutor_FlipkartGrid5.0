#include<Servo.h>

Servo bottomServo;
Servo leftelbow;
Servo griper;
Servo rightelbow;

int inbyte = '0';

int bottomValue = 0;
int leftValue = 90;
int griperValue = 0;
int rightValue = 90;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  
  bottomServo.attach(6);
  leftelbow.attach(9);
  rightelbow.attach(10);
  griper.attach(11);
  pinMode(7,OUTPUT);
  bottomServo.write(0);
  leftelbow.write(90);
  rightelbow.write(90);
  griper.write(0);
}

void loop() {
    if(Serial.available()>0){
      inbyte = Serial.read();
      if(inbyte == 'r'){
        bottomValue = bottomValue - 10;
        bottomServo.write(bottomValue);
      }
      if(inbyte == 'l'){
        bottomValue = bottomValue + 10;
        bottomServo.write(bottomValue);
      }
      if(inbyte == 'c'){
        leftValue = leftValue + 3;
        leftelbow.write(leftValue);
      }
      if(inbyte == 'd'){
        leftValue = leftValue - 3;
        leftelbow.write(leftValue);
      }
      if(inbyte == 'g'){
        griperValue = 50;
        griper.write(griperValue);
      }
      if(inbyte == 'p'){
        griperValue = 0;
        griper.write(griperValue);
      }
      if(inbyte == 'z'){
        rightValue = rightValue + 10;
        rightelbow.write(rightValue);
  
      }
      if(inbyte == 'x'){
        rightValue = rightValue - 10;
        rightelbow.write(rightValue);
        digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
        delay(100);                       // wait for a second
        digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
        delay(100);
        digitalWrite(7,HIGH);
        
      }
    }
}
