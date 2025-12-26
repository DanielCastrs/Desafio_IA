#vamos receber dois dados diferentes do usuario e concatena-los em uma unica string
def concatena_dados(dado1, dado2):
    return str(dado1) + str(dado2)

#exemplo de uso
if __name__ == "__main__":
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    resultado = concatena_dados(dado1, dado2)
    print("Dados concatenados:", resultado)