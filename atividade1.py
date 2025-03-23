'''cultura = str
def calculos(area_e_insumo):
    calculo_tomate = A * W
    calculo_cafe = 3.14 * (R ** 2)

def calcular_manejo(cultura, produto, quantidade_por_metro, ruas):
    return quantidade_por_metro * ruas

def menu():
    print("\n1. Cadastrar Informações")
    print("2. Exibir Dados da Lavoura")
    print("3. Atualizar Informações")
    print("4. Remover Registro")
    print("5. Finalizar Sistema\n")

def cadastrar_informacoes():
    cultura = str(input("Escolha uma cultura (cafe ou tomate): "))
    if cultura == "tomate":
            A = float(input("Digite o comprimento da área de plantio: "))
            W = float(input("Largura do canteiro: "))
            produto = input("Digite o produto a ser aplicado: ")
            quantidade_por_metro = float(input("Digite a quantidade por metro (em mL): "))
            ruas = int(input("Digite o número de ruas: "))
    elif cultura == 'cafe':
            R = float(input("Digite o raio do circulo: "))
            produto = input("Digite o produto a ser aplicado: ")
            quantidade_por_metro = float(input("Digite a quantidade por metro (em mL): "))
            ruas = int(input("Digite o número de ruas: "))
    elif cultura not in CULTURAS:
            print("Cultura inválida!")
            return


def exibir_dados():
    print("1. Ver dados do tomate")
    print("2. Ver dados do cafe")
    str(input("Escolha uma cultura: "))
    if cultura == "tomate":
        print("A área do tomate é {}".format(calculo_tomate))
    elif cultura == "cafe":
        print("A área do café é {}".format(calculo_cafe))

def atualizar_dados():
    exibir_dados()

def remover_registro():
    exibir_dados()


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_informacoes()
    elif opcao == "2":
        exibir_dados()
    elif opcao == "3":
        atualizar_dados()
    elif opcao == "4":
        remover_registro()
    elif opcao == "5":
        print("\n Finalizando o sistema... Até mais!")
        break
    else:
        print("\n Opção inválida! Escolha um número de 1 a 5.")'''

import os

dados_lavoura = {}
while True:
    print("\n" * 100)
    print("\n1. Cadastrar Informações")
    print("2. Exibir Dados da Lavoura")
    print("3. Atualizar Informações")
    print("4. Remover Registro")
    print("5. Finalizar Sistema\n")

    op = int(input("Escolha uma opção: "))

    if op == 1:
        cultura = str(input("Escolha uma cultura (café ou tomate): ")).lower()

        if cultura == "tomate":
            comprimento = float(input("Digite o comprimento da área de plantio (m): "))
            largura = float(input("Largura do canteiro (m): "))
            produto = input("Digite o produto a ser aplicado: ")
            quantidade_por_metro = float(input("Digite a quantidade por metro (em mL): "))
            ruas = int(input("Digite o número de ruas: "))
            area_tomate = comprimento * largura
            insumo_tomate = quantidade_por_metro * ruas
            dados_lavoura["tomate"] = {
                "comprimento": comprimento,
                "largura": largura,
                "area": area_tomate,
                "produto": produto,
                "quantidade_por_metro": quantidade_por_metro,
                "ruas": ruas,
                "insumo_total": insumo_tomate
            }

        elif cultura == "café" or cultura == "cafe":
            raio = float(input("Digite o raio do círculo: "))
            produto = input("Digite o produto a ser aplicado: ")
            quantidade_por_metro = float(input("Digite a quantidade por metro (em mL): "))
            ruas = int(input("Digite o número de ruas: "))
            area_cafe = 3.14 * (raio ** 2)
            insumo_cafe = quantidade_por_metro * ruas
            dados_lavoura["café"] = {
                "raio": raio,
                "area": area_cafe,
                "produto": produto,
                "quantidade_por_metro": quantidade_por_metro,
                "ruas": ruas,
                "insumo_total": insumo_cafe
            }
        else:
            print("Cultura inválida! Tente novamente")
            continue

        print("Dados inseridos com sucesso!")
        input("Pressione Enter para continuar...")

    elif op == 2:
        if not dados_lavoura:
            print("Nenhuma informação cadastrada ainda!")
            input("Pressione Enter para continuar...")
            continue

        cultura_escolhida = input("Escolha uma cultura para exibir (café ou tomate): ").lower()
        if cultura_escolhida in dados_lavoura:
            print(f"\nDados da cultura {cultura_escolhida}:")
            for chave, valor in dados_lavoura[cultura_escolhida].items():
                print(f"{chave.capitalize()}: {valor}")
        else:
            print("Cultura não cadastrada!")
        input("Pressione Enter para continuar...")

    elif op == 3:
        cultura = input("Digite a cultura que deseja atualizar (café ou tomate): ").lower()
        if cultura in dados_lavoura:
            if cultura == "tomate":
                comprimento = float(input("Digite o novo comprimento da área de plantio (m): "))
                largura = float(input("Digite a nova largura do canteiro (m): "))
                quantidade_por_metro = float(input("Digite a nova quantidade por metro (em mL): "))
                ruas = int(input("Digite o novo número de ruas: "))
                dados_lavoura[cultura]["comprimento"] = comprimento
                dados_lavoura[cultura]["largura"] = largura
                dados_lavoura[cultura]["area"] = comprimento * largura
                dados_lavoura[cultura]["quantidade_por_metro"] = quantidade_por_metro
                dados_lavoura[cultura]["ruas"] = ruas
                dados_lavoura[cultura]["insumo_total"] = quantidade_por_metro * ruas
            elif cultura == "café":
                raio = float(input("Digite o novo raio do círculo: "))
                quantidade_por_metro = float(input("Digite a nova quantidade por metro (em mL): "))
                ruas = int(input("Digite o novo número de ruas: "))
                dados_lavoura[cultura]["raio"] = raio
                dados_lavoura[cultura]["area"] = 3.14 * (raio ** 2)
                dados_lavoura[cultura]["quantidade_por_metro"] = quantidade_por_metro
                dados_lavoura[cultura]["ruas"] = ruas
                dados_lavoura[cultura]["insumo_total"] = quantidade_por_metro * ruas
            print("Dados atualizados com sucesso!")
        else:
            print("Cultura não cadastrada!")
        input("Pressione Enter para continuar...")

    elif op == 4:
        cultura = input("Digite a cultura que deseja remover (café ou tomate): ").lower()
        if cultura in dados_lavoura:
            del dados_lavoura[cultura]
            print("Registro removido com sucesso!")
        else:
            print("Cultura não encontrada!")
        input("Pressione Enter para continuar...")

    elif op == 5:
        print("Finalizando o sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")
        input("Pressione Enter para continuar...")