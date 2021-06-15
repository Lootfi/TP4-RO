import numpy as np

# question 1


def check_vecteur_stochatique(vecteur):
    if sum(vecteur) == 1:
        return True
    else:
        return False

# question 2


def check_matrice_caree(matrice):
    for v in matrice:
        if len(v) != len(matrice):
            return False
        else:
            continue
    return True


def check_matrice_stochatique(matrice):
    caree = check_matrice_caree(matrice)
    if caree == False:
        return IndexError("Matrice n'est pas carée")
    for v in matrice:
        if check_vecteur_stochatique(v) == False:
            return False
        else:
            continue
    return True

# question 3


def power_of_matrice(matrice, power):
    if check_matrice_caree(matrice) == False:
        return IndexError("Matrice non carée")
    if check_matrice_stochatique(matrice) == False:
        return IndexError("Matrice non stochatique")

    np_matrice = np.array(matrice)
    powered = np.linalg.matrix_power(np_matrice, power)

    return powered
