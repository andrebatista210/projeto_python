"""Módulo contendo exercícios e exemplos de lógica em Python."""


# import math

# num = 0
# for _ in range(2):
#     num += int(input("Digite o número para soma: "))

# print(f"O resultado é: {num}")

# num_1 = int(input("Digite o primeiro número para soma: "))
# num_2 = int(input("Digite o segundo número para soma: "))

# tot = num_1 + num_2
# print(f"O resultado da soma {num_1} + {num_2} é igual a {tot}")

# num_1 = int(input("Digite o número que será dividido por 5 e saiba o resto: "))
# tot = num_1 % 5
# print(f"O resto da divisão de {num_1} por 5 é igual a {tot}")

# num_1 = int(input("Digite o primeiro número para multiplicação: "))
# num_2 = int(input("Digite o segundo número para multiplicação: "))

# tot = num_1 * num_2
# print(f"O resultado da multiplicação {num_1} x {num_2} é igual a {tot}")

# num_1 = int(input("Digite o primeiro número (dividendo): "))
# num_2 = int(input("Digite o segundo número (divisor): "))

# tot = num_1 // num_2
# print(f"O resultado da divisão inteira {num_1} // {num_2} é {tot}")

# num_1 = int(input("Digite um número para saber o quadrado: "))
# tot = num_1 * num_1
# print(f"O quadrado de {num_1} é igual a {tot}")

# num_1 = int(input("Digite um número para saber o quadrado: "))
# tot = pow(num_1, 2)
# print(f"O quadrado de {num_1} é igual a {tot}")

try:
    num_1 = int(input("Digite o primeiro número (dividendo): "))
    num_2 = int(input("Digite o segundo número (divisor): "))

    tot = num_1 // num_2  # Divisão inteira
    print(f"O resultado da divisão inteira {num_1} // {num_2} é {tot}")

except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
except ValueError:
    print("Erro: digite apenas números inteiros.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
