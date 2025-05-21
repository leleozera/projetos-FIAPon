import requests

API_KEY = "e213356ed7f255883294bcd1d8e34f2d"

# Lista de cidades com nomes reconhecidos pela API
cidades = {
    1: "São Paulo,BR",
    2: "Cotia,BR",
    3: "Rio de Janeiro,BR",
    4: "Belo Horizonte,BR"
}

def obter_dados_climaticos(nome_cidade):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={nome_cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        temperatura = dados["main"]["temp"]
        umidade = dados["main"]["humidity"]
        condicao = dados["weather"][0]["main"]
        return temperatura, umidade, condicao
    else:
        print("❌ Erro ao buscar dados da API.")
        return None, None, None

def verificar_irrigacao(umidade, condicao):
    if condicao.lower() == "rain":
        return "🌧️ Previsão de chuva detectada. Irrigação DESATIVADA."
    elif umidade > 80:
        return "💧 Umidade alta detectada. Irrigação DESNECESSÁRIA."
    else:
        return "🌞 Sem chuva prevista. Irrigação ATIVADA."

def exibir_menu():
    print("\n--- Menu de Cidades ---")
    for opcao, nome in cidades.items():
        print(f"{opcao} - Ver clima em {nome.split(',')[0]}")

def main():
    while True:
        exibir_menu()
        try:
            escolha = int(input("Escolha uma opção (ou 0 para sair): "))
            if escolha == 0:
                print("Saindo do sistema...")
                break
            elif escolha in cidades:
                nome_cidade = cidades[escolha]
                print(f"\nBuscando dados para {nome_cidade.split(',')[0]}...")
                temperatura, umidade, condicao = obter_dados_climaticos(nome_cidade)
                if temperatura is not None:
                    print(f"🌡️ Temperatura: {temperatura}°C")
                    print(f"💧 Umidade: {umidade}%")
                    print(f"☁️ Condição: {condicao}")
                    decisao = verificar_irrigacao(umidade, condicao)
                    print(f"🚿 Decisão de Irrigação: {decisao}")
            else:
                print("⚠️ Opção inválida. Tente novamente.")
        except ValueError:
            print("⚠️ Digite um número válido.")

if __name__ == "__main__":
    main()
