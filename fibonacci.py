def sequencia_fibonacci(n):
    sequence = [0, 1]
    while True:
        next_value = sequence[-1] + sequence[-2]
        if next_value > n:
            break
        sequence.append(next_value)
    return sequence

def pertence(n):
    if n < 0:
        return False
    fib_sequence = sequencia_fibonacci(n)
    return n in fib_sequence

# Solicita um número ao usuário
try:
    num = int(input("Informe um número: "))
    if pertence(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, informe um número válido.")
