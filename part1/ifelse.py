home = "Казахстан"
if home == "Казахстан":
    print("Привет, Казахстан!")
elif home == "Россия":
    print("Привет, Россия!")
else:
    print("Привет, мир!")

print("""Много строк
в 
этой 
переменной""")

x = 10
if x < 10:
    print("x less than 10")
elif x == 10:
    print("x equal 10")
else:
    print("x greater than 10")

y = -10000
if y <= 10:
    print("y less or equal 10")
elif y > 10 and y <= 25:
    print("y greater than 10 but less or equal 25")
elif y > 25:
    print("y greater than 25")

a = 100
b = 51

print(a//b)
print(a%b)
