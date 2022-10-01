import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    level = int(input("Select level: "))
    if level == 1 or level == 2 or level == 3:
        return(level)
    else:
        get_level()


def generate_integer(level):
    if level == 1:
        i1 = 1
        i2 = 9
    elif level == 2:
        i1 = 10
        i2 = 99
    elif level == 3:
        i1 = 100
        i3 = 999

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


if __name__ == "__main__":
    main()
