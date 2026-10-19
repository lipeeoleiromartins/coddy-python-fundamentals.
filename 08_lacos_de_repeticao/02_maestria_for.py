# Módulo de Laços de Repetição - Maestria de For (Contar pares de 10 a 50)
count_even = 0
for i in range(10, 51):
    if i % 2 == 0:
        count_even += 1

print(f"count_even = {count_even}")
