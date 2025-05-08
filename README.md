# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Enterprise Challenge - Sprint 1 - Reply 

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Nunes Urbano 1</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Erick Souza Pereira 2</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>

## 📜 Descrição

Problema: Este projeto simula uma solução de monitoramento inteligente para prevenir falhas em motores industriais, utilizando dados de temperatura e vibração coletados por sensores integrados ao ESP32 (ou simulados via Python). Motores elétricos são comuns em linhas de produção. Um aumento incomum de temperatura ou vibração pode indicar desgaste, sobrecarga ou falha iminente. Motores industriais estão presentes em quase todas as linhas de produção. Falhas inesperadas nesses equipamentos causam paralisações, perdas operacionais e custos com manutenção corretiva.

Solução: Monitorar esses dois fatores já é suficiente para prever falhas com boa precisão. Monitorando continuamente essas variáveis, podemos detectar anormalidades e agir antes da quebra, reduzindo custos e melhorando a eficiência.

## 🧑‍💻 Tecnologias
-  Dados serão coletados a partir de sensores: ESP32

-  Dados serão armazenados em um banco de dados local

-  Integração com modelos de IA: TensorFlow

-  Processamento acontecerá em um computador local

## 📈 Diagrama

![image](https://github.com/user-attachments/assets/039fc19c-f1d1-469d-8e20-b77a47b1670b)


## 📥 Estratégia de Coleta de Dados

A coleta de dados será realizada por meio de um dispositivo ESP32, que estará equipado com sensores de temperatura (como o DHT11 ou DHT22) e vibração (como o SW-420 ou acelerômetro MPU6050). Essa estratégia simula um cenário real de monitoramento em uma linha de produção industrial, onde a variação anormal de temperatura ou vibração pode indicar uma falha iminente em equipamentos.

## 🧑‍🤝‍🧑 Divisão de responsabilidade entre membros

- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Nunes Urbano</a> = Coleta de dados, banco de dados e programação em python
- <a href="https://www.linkedin.com/company/inova-fusca">Erick Souza Pereira</a> = Modelagem de IA, dashboard e programação em python

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

