def sum(lista):
    if len(lista) == 0:
        raise ValueError
    summa = 0
    for i in lista:
        summa += i
    return summa

def min(lista):
    if len(lista) == 0:
        raise ValueError
    mini = None
    for i in lista:
        if mini is None or mini > i:
             mini = i
    return mini


def max(lista):
    if len(lista) == 0:
        raise ValueError
    maxi = None
    for i in lista:
        if maxi is None or maxi < i:
            maxi = i
    return maxi

def average(lista):
    if len(lista) == 0:
        raise ValueError
    tal = 0
    summa = 0.0
    for i in lista:
        tal += 1
        summa += i
    medelvarde = summa/tal
    return medelvarde

def median(lista):
    if len(lista) == 0:
        raise ValueError
    antal_saker = len(lista)
    median = antal_saker/2
    if antal_saker % 2 == 1:
        return sorted(lista)[median]
    elif len(lista) == 1:
        return lista[0]
    else:
        value_nonfloat_h = median
        value_nonfloat_v = median - 1
        median_nonfloatlist = (sorted(lista)[value_nonfloat_v] + sorted(lista)[value_nonfloat_h])/2.0
        return median_nonfloatlist


