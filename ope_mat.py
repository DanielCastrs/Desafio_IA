# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def operacao_simples(num1, num2, operacao):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"
      
# exemplo de uso
if __name__ == "__main__":
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")
    resultado = operacao_simples(numero1, numero2, operacao)
    print("Resultado:", resultado)