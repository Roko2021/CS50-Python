h = input("Expression: ")

x, y, z = h.split(" ")

xf = float(x)
zf = float(z)

if y == "+" :
    answer = xf + zf
if y == "-" :
    answer = xf - zf
if y == "*" :
    answer = xf * zf
if y == "/" :
    answer = xf / zf

print(round(answer ,1))