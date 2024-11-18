# def main():
#     x = input("what time is it? ")
    
#     time = convert(x)
    
#     if time >= 7 and time <= 8 :
#         print("breakfast time")
#     if time >= 12 and time <= 13 :
#         print("lunch time")
#     if time >= 18 and time <= 19 :
#         print("dinner time")


# def convert(time):
#     a, s = time.split(":")
#     zs = float(s) / 60
#     return float(a) + zs

# if __name__ == "__main__":
#     main()
def main():
    answer = input("what time is it? ")

    time = convert(answer)

    if time >= 7 and time <= 8:
        print ("breakfast time")

    if time >= 12 and time <= 13:
        print ("lunch time")

    if time >= 18 and time <= 19:
        print ("dinner time")

def convert(time):

    hours, minutes = time.split(':')
    new_minutes = float(minutes) / 60
    return float(hours) + new_minutes


if __name__ == '__main__':
    main()