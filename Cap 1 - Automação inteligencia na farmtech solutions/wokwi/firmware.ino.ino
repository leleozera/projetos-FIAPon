#include <DHT.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define PIN_FOSFORO 14    // Botão 1 (vermelho)
#define PIN_POTASSIO 12   // Botão 2 (azul)
#define PIN_PH 34         // LDR (sensor de pH simulado)
#define PIN_UMIDADE 2     // DHT22 data
#define PIN_RELE 27       // Controle da bomba via relé
#define PIN_LED 2         // LED indicador (através do resistor)

#define DHTTYPE DHT22
DHT dht(PIN_UMIDADE, DHTTYPE);

// LCD I2C - endereço 0x27, 16 colunas, 2 linhas
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("Sistema FarmTech Solutions iniciado!");

  pinMode(PIN_FOSFORO, INPUT_PULLDOWN);
  pinMode(PIN_POTASSIO, INPUT_PULLDOWN);
  pinMode(PIN_PH, INPUT);
  pinMode(PIN_RELE, OUTPUT);
  pinMode(PIN_LED, OUTPUT);

  digitalWrite(PIN_RELE, LOW);
  digitalWrite(PIN_LED, LOW);

  dht.begin();
  lcd.init();
  lcd.backlight();

  randomSeed(analogRead(34));  // Para gerar valores mais variados
}

void loop() {
  // Leitura dos sensores simulados
  bool fosforoPresente = digitalRead(PIN_FOSFORO);
  bool potassioPresente = digitalRead(PIN_POTASSIO);

  // Simulação aleatória
  float umidade = random(20, 80);  // 20% a 80%
  float phSimulado = random(40, 90) / 10.0; // 4.0 a 9.0

  // Exibição no Serial Monitor
  Serial.print("Fósforo: "); Serial.print(fosforoPresente ? "Sim" : "Não");
  Serial.print(" | Potássio: "); Serial.print(potassioPresente ? "Sim" : "Não");
  Serial.print(" | pH: "); Serial.print(phSimulado, 1);
  Serial.print(" | Umidade: "); Serial.print(umidade, 1); Serial.println("%");

  // Critérios para irrigação
  bool ativarIrrigacao = !fosforoPresente || !potassioPresente || umidade < 40.0 || phSimulado < 5.5 || phSimulado > 7.5;

  digitalWrite(PIN_RELE, ativarIrrigacao ? HIGH : LOW);
  digitalWrite(PIN_LED, ativarIrrigacao ? HIGH : LOW);
  Serial.println(ativarIrrigacao ? ">>> Irrigação ATIVADA" : ">>> Irrigação DESATIVADA");

  // Gráfico no Serial Plotter
  Serial.print("umidade:\t");
  Serial.print(umidade);
  Serial.print("\tph:\t");
  Serial.print(phSimulado);
  Serial.print("\tirrigacao:\t");
  Serial.println(ativarIrrigacao ? 1 : 0);

  // Exibição no LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Umi: "); lcd.print(umidade, 0); lcd.print("% pH:");
  lcd.print(phSimulado, 1);
  lcd.setCursor(0, 1);
  lcd.print(ativarIrrigacao ? "IRRIGACAO ATIVA" : "IRRIGACAO OK");

  delay(2000);
}
