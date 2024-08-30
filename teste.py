def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

numero = int(input("Informe um número: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

def contar_a(s):
    count = s.lower().count('a')
    return count

texto = input("Informe uma string: ")
quantidade_a = contar_a(texto)

if quantidade_a > 0:
    print(f"A letra 'a' ocorre {quantidade_a} vezes na string.")
else:
    print("A letra 'a' não ocorre na string.")

# Código equivalente ao trecho 'enquanto K < INDICE faça {...}' traduzido para Python
INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K += 1
    SOMA += K

print(SOMA)
