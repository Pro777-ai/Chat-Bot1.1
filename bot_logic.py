import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def coin_throw():
    throw = random.randint(0, 1)  # Fix the range to 0-1 for binary choice
    if throw == 0:
        return "CARA"
    else:
        return "CRUZ"
