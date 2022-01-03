import re

pw_possibles = {"digits": 10, "lowercase": 26, "uppercase": 26, "special": 32}

special_charachters = "!'#$%&()*+,-./:;<>=?@[\]^_-`{|}~"
special_charachters += '"'


def check_sc(pw):
    for c in pw:
        if c in special_charachters:
            return True
    return False

pw_per_second = 100000000000

pw = ""
possibles = 0

seconds_in_year = 60 * 60 * 24 * 365
seconds_in_week = 60 * 60 * 24 * 7
seconds_in_month = 60 * 60 * 24 * 30

seconds_in_day = 60 * 60 * 24
seconds_in_hour = 60 * 60
seconds_in_minute = 60



while pw != "stop":
    possibles = 0
    kinds = []

    pw = input("PAsswort zum checken eingeben: ")
    if re.search(r'\d', pw):
        kinds.append("digits") 
        possibles += 10
    if re.search('[a-z]+', pw):

        kinds.append("lowercase") 
        possibles += 26
    if re.search('[A-Z]+', pw):
        kinds.append("uppercase") 
        possibles += 26
    if check_sc(pw):
        kinds.append("special") 
        possibles += 32
    print("Das Passwort enthält: ", kinds)
    seconds = (possibles**len(pw))/pw_per_second
    #seconds = seconds_in_year + seconds_in_month + seconds_in_week + seconds_in_day + seconds_in_hour + seconds_in_minute + 1
    years = seconds // seconds_in_year
    months = (seconds - (years * seconds_in_year)) // seconds_in_month
    weeks = (seconds - (years * seconds_in_year) - (months * seconds_in_month)) // seconds_in_week
    days = (seconds- (years * seconds_in_year) - (months * seconds_in_month) - (weeks * seconds_in_week)) // seconds_in_day
    hours = (seconds - (years * seconds_in_year) - (months * seconds_in_month) - (weeks * seconds_in_week) - (days * seconds_in_day)) // seconds_in_hour
    minutes = (seconds - (years * seconds_in_year) - (months * seconds_in_month) - (weeks * seconds_in_week) - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute
    seconds = seconds - (years * seconds_in_year) - (months * seconds_in_month) - (weeks * seconds_in_week) - (days * seconds_in_day) - (hours * seconds_in_hour) - (minutes * seconds_in_minute)
    print("Sekunden: ", seconds)
    print("Minuten: ", minutes)
    print("Stunden: ", hours)
    print("Tage: ", days)
    print("Wochen: ", weeks)
    print("Monate: ", months)
    print("Jahre: ", years)
