#include <DHT.h>

#define PIN_FOSFORO 14    // Botão 1
#define PIN_POTASSIO 12   // Botão 2
#define PIN_PH 34         // LDR (sensor de pH simulado)
#define PIN_UMIDADE 2     // DHT22 data
#define PIN_RELE 27       // Controle da bomba via relé
#define PIN_LED 2         // LED indicador (através do resistor)

#define DHTTYPE DHT22

DHT dht(PIN_UMIDADE, DHTTYPE);

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("Sistema FarmTech Solutions iniciado!");

  pinMode(PIN_FOSFORO, INPUT_PULLDOWN);   // Botões com pull-down interno
  pinMode(PIN_POTASSIO, INPUT_PULLDOWN);
  pinMode(PIN_PH, INPUT);
  pinMode(PIN_RELE, OUTPUT);
  pinMode(PIN_LED, OUTPUT);

  digitalWrite(PIN_RELE, LOW);  // Desliga bomba inicialmente
  digitalWrite(PIN_LED, LOW);   // LED apagado inicialmente

  dht.begin();
}

void loop() {
  // Leitura dos sensores
  bool fosforoPresente = digitalRead(PIN_FOSFORO);
  bool potassioPresente = digitalRead(PIN_POTASSIO);
  int phAnalogico = analogRead(PIN_PH);
  float umidade = dht.readHumidity();

  // Verifica se leitura do DHT22 falhou
  if (isnan(umidade)) {
    Serial.println("Falha ao ler sensor DHT22");
    delay(2000);
    return;
  }

  // Mapear valor analógico do LDR para faixa de pH 0-14
  float phSimulado = map(phAnalogico, 0, 4095, 0, 14);

  // Mostra os dados no monitor serial
  Serial.print("Fósforo (botao14): "); Serial.print(fosforoPresente ? "Sim" : "Não");
  Serial.print(" | Potássio (botao12): "); Serial.print(potassioPresente ? "Sim" : "Não");
  Serial.print(" | pH simulado (LDR): "); Serial.print(phSimulado, 1);
  Serial.print(" | Umidade (%): "); Serial.print(umidade, 1);
  Serial.println();

  // Critérios para ligar irrigação:
  // - Se faltar fósforo OU potássio
  // - OU umidade < 40%
  // - OU pH fora da faixa ideal 5.5 a 7.5
  if (!fosforoPresente || !potassioPresente || umidade < 40.0 || phSimulado < 5.5 || phSimulado > 7.5) {
    digitalWrite(PIN_RELE, HIGH); // Liga bomba
    digitalWrite(PIN_LED, HIGH);  // LED aceso
    Serial.println(">>> Irrigação ATIVADA");
  } else {
    digitalWrite(PIN_RELE, LOW);  // Desliga bomba
    digitalWrite(PIN_LED, LOW);   // LED apagado
    Serial.println(">>> Irrigação DESATIVADA");
  }

  delay(2000); // Espera 2 segundos entre leituras
}
