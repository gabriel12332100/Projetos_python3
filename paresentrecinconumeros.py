pares = 0
for _ in range(5):
    valor = int(input())
    if valor % 2 == 0:
        pares += 1
print(f"{pares} valores pares")
