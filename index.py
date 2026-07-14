name = input("Enter name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))
power = int(input("Enter power: "))
starter_dollar = float(input("Enter starter pack dollar"))

if power >= 1000000:
    print("ผ่าน")
elif power >= 5000:
    print("ผ่านแต่เงินเดือน 20")
else:
    print("ไม่ผ่าน")
