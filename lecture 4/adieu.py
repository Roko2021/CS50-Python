import inflect

p = inflect.engine()

x = []

while True:
    try:
        y = input("Name: ")
        x.append(y)
    except:
        print()
        break
    
last = p.join(x)
print("Adieu, adieu, to " + last)