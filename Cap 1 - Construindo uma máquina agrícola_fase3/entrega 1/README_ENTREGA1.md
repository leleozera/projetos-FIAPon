# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Sistema de Irrigação Inteligente com ESP32

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Nunes Urbano 1</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Erick Souza Pereira 2</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>

## 📜 Descrição

Este projeto implementa um sistema inteligente de irrigação utilizando sensores físicos simulados na plataforma Wokwi e um microcontrolador ESP32. O sistema coleta dados de sensores de fósforo, potássio, pH e umidade do solo, e aciona automaticamente uma bomba de irrigação (simulada por um módulo relé) conforme a lógica definida.

A lógica de controle considera a presença de nutrientes essenciais e valores ideais de pH e umidade para ativar ou desativar a irrigação automaticamente, promovendo o uso eficiente de água e insumos na agricultura.

## 🧠 Sensores Simulados

- **Fósforo (P):** Botão (pressionado = presente)
- **Potássio (K):** Botão (pressionado = presente)
- **pH:** Sensor LDR (representa variações contínuas de pH)
- **Umidade:** Sensor DHT22 (retorna umidade real)
- **Relé:** Aciona bomba de irrigação (simulada)
- **LED:** Representa o status da irrigação (ligado = irrigando)

## 🔧 Como executar o código

Requisitos:
- Plataforma [Wokwi](https://wokwi.com/)
- Extensões: Wokwi + PlatformIO no VS Code

Passos:
1. Importe o arquivo `diagram.json` no Wokwi;
2. Copie e cole o código `main.cpp`;
3. Simule a leitura dos sensores e observe a ativação do relé conforme a lógica implementada;
4. O LED se acende sempre que a irrigação estiver ativa.

## 🖼️ Imagem do circuito

<p align="center">
 ![Screenshot_2](https://github.com/user-attachments/assets/79c381c6-516b-4c35-82dc-c1f07af75a6a)

</p>

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
