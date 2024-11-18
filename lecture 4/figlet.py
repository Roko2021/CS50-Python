import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    x = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    x = False
else:
    sys.exit(1)
    
y = input("Input: ")

figlet.getFonts()

if x == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())


print("Output: ")
print(figlet.renderText(y))