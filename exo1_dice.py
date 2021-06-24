import random as r
import argparse
parser = argparse.ArgumentParser()


# question 1


def dice_simulation():
    return r.randrange(1, 7)

# question 2


def multiple_throws_simulation(n):
    liste = []
    for i in range(n):
        liste.append(dice_simulation())
    return liste

# question 3


def count_sixes(liste):
    return liste.count(6)

# question 4


def launches_before_six(liste):
    for i, launch in enumerate(liste, 0):
        if launch == 6:
            return i
    return -1


parser.add_argument("-n", "--number", help="Number of dice throws", type=int)
parser.add_argument("-b", "--before_six", action='store_true',
                    help="Count throws before getting a 6")
parser.add_argument("-a", "--apparition_six", action='store_true',
                    help="Count the apparition of 6")
args = parser.parse_args()

liste = multiple_throws_simulation(args.number)
print(liste)

if(args.before_six):
    bs = launches_before_six(liste)
    if(bs == -1):
        print("On a pas obtenu des 6s")
    else:
        print("Nombre de lancers avant obtenir le premier 6:", bs)

if(args.apparition_six):
    print("apparitions de 6:", count_sixes(liste))
