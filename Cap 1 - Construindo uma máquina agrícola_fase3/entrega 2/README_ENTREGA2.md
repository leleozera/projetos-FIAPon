# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Armazenamento e Análise de Dados de Irrigação com Python + SQL

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

Este módulo do projeto simula o armazenamento de dados coletados via ESP32 em um banco de dados SQLite usando Python. A base de dados permite armazenar leituras de fósforo, potássio, pH, umidade e status da irrigação, além de realizar operações completas de CRUD (Create, Read, Update, Delete).

A proposta facilita a posterior análise dos dados, identificação de padrões e controle histórico das condições do solo, fornecendo um sistema inteligente e escalável para aplicações agrícolas reais.

## 🧩 Relação com o MER

A tabela `leituras` representa a entidade principal "SensorData", conforme modelado na fase 2 do projeto. Cada registro corresponde a uma amostra coletada com timestamp e atributos quantitativos.

## 🔧 Como executar o código

Requisitos:
- Python 3.10+
- Bibliotecas:
  - `sqlite3` (nativa)
  - `datetime` (nativa)

Passos:
1. Execute o script `sensor_data_sqlite.py`
2. Acompanhe as inserções e operações CRUD no terminal
3. Os dados são armazenados em um arquivo `dados_sensores.db`

## ✨ Operações CRUD

- `inserir_leitura(...)`: cria uma nova entrada
- `consultar_todas()`: lê todas as leituras
- `atualizar_umidade(id, nova_umidade)`: atualiza campo específico
- `apagar_leitura(id)`: exclui leitura por ID

## 📊 Exemplo de tabela preenchida

| id | timestamp           | fósforo | potássio | pH    | umidade | irrigação |
|----|---------------------|---------|----------|-------|---------|------------|
| 1  | 2025-05-20 10:10:00 |    1    |    1     | 6.0   | 45.0    |     1      |

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>