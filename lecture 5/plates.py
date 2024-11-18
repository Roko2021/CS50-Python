def main():
    plate = input('plate: ')
    if is_valid(plate):
        print('valid')
    else:
        print('invalid')
    
    
def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha == False:
        return False
    
    i = 0
    while i < len(s):
        
    



if __name__ == '__main__':
    main()