import time
import random

def attesa():
    tempo = random.randint(1, 200)
    return tempo


def monetina():
    numero = random.randint(1, 100)
    if numero % 2 == 0:
        return 1
    else:
        return 0
