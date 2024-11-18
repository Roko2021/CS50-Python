from validator_collection import validators

def main():
    email_adress = input("what's your email address? ")
    try:
        emailsvaild = validators.email(email_adress)
        print('Valid')
    except:
        print('Invalid')
    
if __name__ == '__main__':
    main()