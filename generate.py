# generate random eurojackpot row
from random import seed
from random import randint
import random
import sys


def generate_row():
    generated_row = []
    seed_value = random.randrange(sys.maxsize)
    seed(seed_value)

    used_numbers = []
    n = 0
    while True:
        if n == 5:
            used_numbers.clear()
        if n > 6:
            break
        else:
            x = 50 if n < 5 else 10
            value = randint(1, x)
            if value not in used_numbers:
                generated_row.insert(n, value)
                used_numbers.insert(n, value)
                n += 1

    return generated_row
