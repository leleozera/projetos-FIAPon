# Desafio Hermes Reply – Fase 4

Este projeto simula um sistema de monitoramento inteligente de motores industriais, utilizando sensores virtuais conectados a uma placa ESP32 no ambiente de simulação Wokwi.

## 🔧 Objetivo

Monitorar variáveis que indicam possíveis falhas em motores, como:
- Temperatura e umidade (DHT22)
- Vibração (MPU6050)
- Luminosidade (LDR)
- Presença de gases (MQ-2)

## 🧩 Sensores Utilizados

| Sensor     | Finalidade                                         |
|------------|----------------------------------------------------|
| DHT22      | Mede temperatura e umidade                         |
| MPU6050    | Detecta vibrações (aceleração nos eixos X, Y, Z)   |
| LDR        | Mede luminosidade ambiente (simula presença de luz no motor) |
| MQ-2       | Detecta gases (simula vazamentos ou superaquecimento)       |

## 💻 Simulação

- Plataforma: [Wokwi](https://wokwi.com/)
- Placa: ESP32 DevKit v4

## 📂 Arquivos

-  Codigo fonte – Código .cpp e .json
- Print` – Todas os print da simulação, testes e graficos
- Sensores - Todos os sensores utilizados e justificados


## 🧠 Conclusão

O projeto demonstra um fluxo básico e funcional de coleta e análise de dados com ESP32 e sensores, simulando um ambiente industrial digitalizado. A solução permite prever falhas e aumentar a eficiência da manutenção preditiva.


## 📦 Bibliotecas Utilizadas (com links):
DHTesp
Leitura de temperatura e umidade com sensor DHT22 (compatível com ESP32)

Adafruit MPU6050
Leitura de aceleração e giroscópio do sensor MPU6050

Adafruit Unified Sensor
Biblioteca base para sensores da Adafruit (necessária para o MPU6050)

## 🧪 Caso utilizar o Visual Studio
- PLATIFORMIO.INI
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
monitor_speed = 115200

lib_deps =
https://github.com/beegee-tokyo/DHTesp.git
https://github.com/adafruit/Adafruit_MPU6050.git
https://github.com/adafruit/Adafruit_Sensor.git
