x = input("what is time? ")

y = 0

if "p.m" in x:
    y =+ 12

w = x.replace('p.m','')

a,s = w.split(":")

zs = float(s) / 60

a = float(a) + zs +y

if a == 15:
    print("yes")

print(y)