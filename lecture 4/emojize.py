import emoji

x  = input("Input: ")

emoji = emoji.emojize(x, language='alias')

print("Output: ", emoji)