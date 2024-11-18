def main():
    message = input("Input: ")
    message_without = shorten(message)
    print('Output: ' + message_without)


def shorten(word):
    message_without = ''
    
    for letter in word:
        if letter.lower() in ('a','i','e','o','u'):
            message_without == ''
        else:
            message_without += letter
            
    return message_without
        


if __name__ == "__main__":
    main()
