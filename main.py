def fibonacci(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    if n in sequence:
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")

for i in range(50):
    fibonacci(i)
