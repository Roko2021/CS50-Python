x = input("camelcase: ")

print("snakecase: " , end="")

for i in x:
    if i.isupper():
        print("_" + i.lower() ,end="")
    else:
        print(i,end="")
