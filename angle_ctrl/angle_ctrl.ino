int angle = 0;


void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600); 
  Serial.println("Ready");
}

void loop() {
  while(Serial.available()){ 
    angle = Serial.readString().toInt();
    Serial.println(angle+1);
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(1000);
    Serial.flush();
  }
delay(10); 
}
