quantity = int(input("Enter weapon quantity: "))
cost_price = float(input("Enter cost price: "))
sell_price = float(input("Enter sell price: "))
team_members = int(input("Enter team members count: "))

income = sell_price * quantity
cost = cost_price * quantity
profit = income - cost
boss = profit * 0.2
employee = (profit-boss) / team_members

print("ขายได้: ", quantity)
print("ต้นทุนทั้งหมด", cost)
print("รายรับทั้งหมด", income)
print("กำไรสุทธิ", profit)
print("จำนวนที่หักให้บอส 20%", boss)
print("เงินที่หักไปให้ลูกน้อง: ", employee)