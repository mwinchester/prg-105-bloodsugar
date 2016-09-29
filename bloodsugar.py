# blood sugar levels

sugars = {'9:00': 99, '6:00': 86, '11:30': 123, '13:30': 212, '15:30': 160, '18:00': 143, '20:00': 102}

# global variables
top_range = 120

high = dict()


def ave_bs(day):
    total = 0
    for bs in day:
        total += day[bs]
    ave = total / len(sugars)
    print("Your average blood sugar toady was: " + str(ave))


def over(today):
    global top_range
    for bs in today:
        if today[bs] > top_range:
            high[bs] = (today[bs])
    print high


ave_bs(sugars)
over(sugars)
