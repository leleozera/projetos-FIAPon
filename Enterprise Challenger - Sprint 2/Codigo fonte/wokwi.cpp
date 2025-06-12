
#include <DHTesp.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

const int DHT_PIN = 4;
const int LDR_PIN = 36;  // VP = GPIO36
const int GAS_PIN = 39;  // VN = GPIO39

DHTesp dht;
Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  dht.setup(DHT_PIN, DHTesp::DHT22);

  if (!mpu.begin()) {
    Serial.println("Falha ao iniciar MPU6050!");
    while (1);
  }
}

void loop() {
  TempAndHumidity data = dht.getTempAndHumidity();

  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  int ldr = analogRead(LDR_PIN);
  int gas = analogRead(GAS_PIN);

  Serial.print("Temp: ");
  Serial.print(data.temperature);
  Serial.print("°C | Umidade: ");
  Serial.print(data.humidity);
  Serial.print("% | AcelX: ");
  Serial.print(a.acceleration.x);
  Serial.print(" m/s² | LDR: ");
  Serial.print(ldr);
  Serial.print(" | Gás: ");
  Serial.println(gas);

  delay(2000);
}
