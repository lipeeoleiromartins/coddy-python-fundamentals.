print("Bill Split Calculator")

bill_amount = float(input())
tip_percentage = float(input())
num_people = int(input())

tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
cost_per_person = total_amount / num_people

print(total_amount)
print(cost_per_person)
