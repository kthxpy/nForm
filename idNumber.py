import re

def isFormatValid(number):
    if len(number) != 11:
        return False
    if number[6] != "/":
        return False
    for i in range(11):
        if i == 6:
            continue
        if not number[i].isdigit():
            return False

    return True

def isDivisibleby11(number):
    number = list(number)
    number.pop(6)
    number = "".join(number)
    number = int(number)
    mod = number % 11

    if mod == 0:
        return True
    else:
        return False

def maleOrFemale(number):
    if int(number[2:4]) > 12:
        return "žena"
    else:
        return "muž"

def birthDate(number):
    year = 0
    month = 0
    day = 0
    if maleOrFemale(number) == "žena":
        mod1 = int(number[2:4])% 70
        print(mod1)
        if mod1 == 0:
            month = int(number[2:4]) - 70
        else:
            month = int(number[2:4]) - 50
    else:
        month = int(number[2:4])

    day = int(number[4:6] )
    year = int(number[0:2])

    return(day, month, year )


def birthNumberStat():
    return
