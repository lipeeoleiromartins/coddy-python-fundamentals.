# 04. Maestria de If - Else (Classificação de Temperatura)
temperature = int(input())
weather = "unset"

if temperature < 0:
    weather = "Freezing"
elif temperature <= 15:
    weather = "Cold"
elif temperature <= 25:
    weather = "Mild"
else:
    weather = "Hot"

print(f"weather = {weather}")
