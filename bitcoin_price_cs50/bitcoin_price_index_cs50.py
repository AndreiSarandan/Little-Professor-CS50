<<<<<<< HEAD
<<<<<<< HEAD
import requests

try:
    # extract bitcoin price value
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json = r.json()
    z = (json['bpi']['USD']['rate'])
    print(z)
except requests.RequestException:
    print("error")
=======
import random


def main():
    lvl = get_level()
    generate_integer(lvl)


def get_level():
    while True:
        try:
            level = int(input("Select level: "))
            break
        except ValueError:
            pass
    if level != 1 and level != 2 and level != 3:
        get_level()
    return level


def generate_integer(level):
    score = 10
    if level == 1:
        i1 = 0
        i2 = 9
    elif level == 2:
        i1 = 10
        i2 = 99
    elif level == 3:
        i1 = 100
        i2 = 999

    for i in range(10):
        ok = 0
        x = random.randint(i1, i2)
        y = random.randint(i1, i2)
        for i in range(3):
            print(f'{x} + {y} =')
            s = int(input())
            if(s == x+y):
                ok = 1
                break
            else:
                print("EEE")
        if ok == 0:
            print(x+y)
            score -= 1
    print(score)


if __name__ == "__main__":
    main()
>>>>>>> parent of 3c5aa4d (Rename bitcoin_price_index_cs50.py to Little Professor CS50)
=======
import requests

try:
    # extract bitcoin price value
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json = r.json()
    z = (json['bpi']['USD']['rate'])
    print(z)
except requests.RequestException:
    print("error")
>>>>>>> parent of 0ba68ec (Update bitcoin_price_index_cs50.py)
