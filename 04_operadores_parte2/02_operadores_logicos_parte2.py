# ==========================================
# Exercícios de Operadores Lógicos Parte 2 - Coddy
# ==========================================

# 1. Comparação de Multiplicação vs Soma
b1 = 2
b2 = 3
b3 = (b1 * b2) > (b1 + b2)
print(f"b3 = {b3}")

# 2. Avaliação de Expressão Booleana
a = True
b = False
c = False
result = (a or b) and not c
print(f"result = {result}")

# 3. Elegibilidade para Dirigir
age = 20
has_license = True
has_insurance = True
is_eligible = age >= 18 and has_license and has_insurance
print(f"Elegível para dirigir: {is_eligible}")

# 4. App de Meteorologia
is_sunny = True
temperature = 25
wind_speed = 10
water_temperature = 22

can_go_hiking = is_sunny and temperature > 15 and wind_speed < 20
can_go_swimming = is_sunny and temperature > 20 and water_temperature > 18
cannot_go_outside = not is_sunny or temperature < 10 or wind_speed > 30

print("Can go hiking:", can_go_hiking)
print("Can go swimming:", can_go_swimming)
print("Cannot go outside:", cannot_go_outside)
