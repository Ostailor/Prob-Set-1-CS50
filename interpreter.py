expression = input("Expression: ").split(" ")
x = int(expression[0])
y = expression[1]
z = int(expression[2])

if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "/":
    print(round(float(x / z), 2))
else:
    print(float(x * z))
