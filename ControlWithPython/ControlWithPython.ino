

void setup() {
  pinMode(13,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()){
    int i=Serial.read();
    Serial.println(i);
    if (i==1)
    digitalWrite(13,1);
    else if(i==0)
    digitalWrite(13,0);
  }

}
