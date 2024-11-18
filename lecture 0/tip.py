def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    x = d.replace('$','')
    return float(x)


def percent_to_float(p):
    # TODO
    z = p.replace('%','')
    c = float(z) / 100
    return c


main()