import random

while True:
    try:
        x = int(input("Level: "))
        if x > 0:
            break
    except:
        pass
y = random.randint(1,x)
while True:
    try:
        z = int(input("Guess: "))
        if z < y:
            print("Too Small!")
        elif z > y:
            print("Too large! ")
        else :
            print("Just right! ")
            break
    except:
        pass