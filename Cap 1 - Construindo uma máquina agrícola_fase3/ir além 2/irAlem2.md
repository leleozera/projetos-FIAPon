
---

### 📄 `README_api.md`

```markdown
# ☁️ Sistema de Decisão de Irrigação com API Climática – FarmTech Solutions

Este projeto demonstra a **integração com a API OpenWeatherMap**, que fornece dados climáticos em tempo real para várias cidades. O sistema usa esses dados para **decidir automaticamente se a irrigação deve ser ativada ou não**, considerando a previsão de chuva e o nível de umidade do ar.

## 🔗 API Utilizada

- [OpenWeatherMap API](https://openweathermap.org/current)
- Endpoint: `https://api.openweathermap.org/data/2.5/weather`
- Formato de resposta: JSON

## 📦 Tecnologias

- Python
- Biblioteca `requests`

## ⚙️ Lógica de Decisão

```python
if condicao.lower() == "rain":
    return "🌧️ Previsão de chuva detectada. Irrigação DESATIVADA."
elif umidade > 80:
    return "💧 Umidade alta detectada. Irrigação DESNECESSÁRIA."
else:
    return "🌞 Sem chuva prevista. Irrigação ATIVADA."
