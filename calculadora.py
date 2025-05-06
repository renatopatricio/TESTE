def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 'Erro: divisão por zero!'
    return a / b

if __name__ == "__main__":
    print("Calculadora Simples")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    escolha = input("Digite o número da operação desejada: ")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(f"Resultado: {soma(a, b)}")
    elif escolha == '2':
        print(f"Resultado: {subtrai(a, b)}")
    elif escolha == '3':
        print(f"Resultado: {multiplica(a, b)}")
    elif escolha == '4':
        print(f"Resultado: {divide(a, b)}")
    else:
        print("Opção inválida!")
