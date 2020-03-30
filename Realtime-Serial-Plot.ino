int sensorValue1,sensorValue2;
void setup() {
  Serial.begin(115200);
}

void loop() {
  sensorValue1 = analogRead(A0);
  sensorValue2 = analogRead(A0)/2;
  Serial.print(sensorValue1);
  /*Serial.print(" ");
  Serial.print(sensorValue2);*/
  Serial.println("");
  delay(50);
}
