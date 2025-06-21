# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%">
  </a>
</p>

<br>


# 📼 Link do video no Youtube: https://youtu.be/8ZTxY27ew34

# 🌱 Projeto FarmTech Solutions  
Sistema de monitoramento automatizado de irrigação baseado em sensores, inteligência artificial e ESP32.

## 👨‍🎓 Integrantes:
- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Nunes Urbano 1</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Erick Souza Pereira 2</a>

## 👩‍🏫 Professores:
### Tutor(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>  
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>

## 📁 Estrutura de Pastas

- `database/`: Contém o banco de dados `sensores.db`, script SQL de criação de tabelas e o arquivo `diagram.json`.
- `python/`: Scripts Python com modelo de predição (`modelo_predict.py`) e dashboard com Streamlit (`streamlit_app.py`).
- `wokwi/`: Diagrama do circuito do ESP32 (`esquema.json`) e o código embarcado (`firmware.ino`).
- `serial_plotter/`: Capturas de tela e registros do comportamento gráfico via Serial Plotter para análise visual.
- `inserir_dados.py` e `criar_tabela.py`: Scripts auxiliares para manipulação e estruturação do banco de dados.

## 🔧 Como Executar o Projeto

**Pré-requisitos:**
- Python 3.8 ou superior instalado
- Ter as bibliotecas necessárias:

```bash
pip install pandas scikit-learn joblib streamlit
