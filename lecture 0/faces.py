def main():
    msg = input()
    result = convert(msg)

    print(result)


def convert(msg):
    msg2 = msg.replace(':)','🙂')
    msg2 = msg.replace(':(','🙁')
    return msg2


main()