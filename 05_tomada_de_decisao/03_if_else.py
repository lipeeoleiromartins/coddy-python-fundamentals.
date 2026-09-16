# 03. If - Else (Velocidade do Vento)
wind = int(input())
status = "unset"

if wind < 8:
    status = "Calm"
elif wind <= 31:
    status = "Breeze"
elif wind <= 63:
    status = "Gale"
else:
    status = "Storm"

print(f"status = {status}")
