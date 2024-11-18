x = input("Input: ")
print("Output: ", end="")

for i in x:
    if i.lower() == "a" or i.lower() == "i" or i.lower() == "e" or i.lower() == "o" or i.lower() == "u":
        print("",end="")
    else:
        print(i,end="")