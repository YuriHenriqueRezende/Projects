#include "DHT.h"
#define DHTPIN A1
#define DHTTYPE DHT12
DHT dht(DHTPIN, DHTTYPE);

void setup(){
  Serial.begin(9600);
  dht.begin();}

void loop(){
  float t = dht.readTemperature();

  Serial.println(t);
  delay(1000);
}
