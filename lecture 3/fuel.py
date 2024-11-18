while True:
    x = input("Fraction: ")
    
    try:
        a,s = x.split("/")
        za = int(a)
        zs = int(s)
        
        w = za / zs
        
        if w <= 1:
            break
        
    except (ValueError, ZeroDivisionError):
        pass
    
h = int(w * 100)

if h <= 1:
    print("E")
elif h >= 99:
    print("F")
else:
    print(f"{h}%")