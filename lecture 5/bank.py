def main():
    greeting = input('Greeting: ')
    value_custom = value(greeting)
    print(f'${value_custom}')
    
def value(greeting):
    greeting = greeting.lower().strip()
    if 'hello' in greeting:
        return 0
    if 'h' == greeting[0]:
        return 20
    else:
        return 100
    
if __name__ == '__main__':
    main()