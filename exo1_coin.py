import random as r
import argparse
parser = argparse.ArgumentParser()

# question 5


def coin_draw():
    return r.randrange(0, 2)


def coin_draws(n):
    liste = []
    for i in range(n):
        liste.append(coin_draw())
    return liste


parser.add_argument("-n", "--number", help="Number of coin tosses", type=int)
args = parser.parse_args()

liste = coin_draws(args.number)
print(liste)
