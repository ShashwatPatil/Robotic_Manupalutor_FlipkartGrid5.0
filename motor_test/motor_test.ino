int leftmotor1=6;
int leftmotor2=7;
int rightmotor1=8;
int rightmotor2=9;
int ENA=5;
int ENB=10;
void setup() {
  // put your setup code here, to run once:
  pinMode(leftmotor1,OUTPUT);
  pinMode(leftmotor2,OUTPUT);
  pinMode(rightmotor1,OUTPUT);
  pinMode(rightmotor2,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);
 

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ENA,255);
  digitalWrite(leftmotor1,HIGH);
  digitalWrite(leftmotor2,LOW);

  digitalWrite(ENB,255);
  digitalWrite(rightmotor1,HIGH);
  digitalWrite(rightmotor2,LOW);
  delay(1);
  

}
