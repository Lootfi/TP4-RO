import random as r

# question 1


def dice_simulation():
    return r.randrange(1, 7)

# question 2


def multiple_throws_simulation(n):
    liste = []
    for i in range(n):
        liste.append(dice_simulation())
    print(liste)
    print(apparition_of_six(liste))

# question 3


def apparition_of_six(liste):
    return liste.count(6)

# question 4


def launches_before_six(n):
    liste = []
    while True:
        d = dice_simulation()
        liste.append(d)
        if d == 6:
            break
    return liste

# question 5


def coin_draw():
    return r.randrange(0, 2)


def coin_draws(n):
    liste = []
    for i in range(n):
        liste.append(coin_draw())
    return liste
