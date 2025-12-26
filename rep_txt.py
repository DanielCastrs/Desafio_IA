# Agora vamos solicitar uma string e um número inteiro como entrada. depois teremos que retornar a string repetida o numero de vezes informado.
def repete_string(string, n):
    return string * n

# exemplo de uso
if __name__ == "__main__":
    entrada_string = input("Digite uma string: ")
    entrada_numero = int(input("Digite um número inteiro: "))
    resultado = repete_string(entrada_string, entrada_numero)
    print("String repetida:", resultado)