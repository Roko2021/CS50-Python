from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birthday = input('Date of Birth: ')
    try:
        year,month,day = check_birthday(birthday)
    except:
        sys.exit('Invalid Date')
    date_of_birthday = date(int(year), int(month), int(day))
    date_of_today = date.today()
    diff = date_of_today - date_of_birthday
    total_age_minit = diff.days * 24 * 60
    out_put = p.number_to_words(total_age_minit,andword="")
    print(out_put.capitalize() + ' minutes')

def check_birthday(birthday):
    if re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$',birthday):
        year,month,day = birthday.split('-')
        return year,month,day


if __name__ == "__main__":
    main()