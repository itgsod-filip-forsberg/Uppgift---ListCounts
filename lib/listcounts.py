def sum(lista):
    summa = 0
    for i in lista:
        summa += i
    return summa

def min(lista):
    mini = None
    for i in lista:
        if mini is None or mini > i:
             mini = i


def max(lista):
    maxi = None
    for i in lista:
        if maxi is None or maxi < i:
            maxi = i

def average(lista):
    tal = 0
    summa = 0
    medelvarde = 0
    for i in lista:
        tal += 1
        summa += i
    medelvarde = summa/tal
    return medelvarde

def median(lista):
    