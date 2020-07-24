# Overview: Enter your password when asked for it and a maximum amount of tries, then wait.

import string
from random import *

pw = input("Enter your Password here: ")
tries = input("How many tries do you want me to go through? : ")

def pwgen(limit):
    k = randint(0, 2)
    max = randint(4, 25)
    if k == 0:
        charactersstrong = string.ascii_letters + string.punctuation  + string.digits
        passwordstrong =  "".join(choice(charactersstrong) for x in range(1, max))
        k = k + 1
        return passwordstrong
    elif k == 1:
        charactersmedium = string.ascii_letters + string.punctuation
        passwordmedium =  "".join(choice(charactersmedium) for x in range(1, max))
        k = k + 1
        return passwordmedium
    elif k == 2:
        charactersweak = string.ascii_letters
        passwordweak =  "".join(choice(charactersweak) for x in range(1, max))
        k = k + 1
        return passwordweak
    else:
        return

def pwtester(check):
    if check == pw:
        return True
    else:
        return False


if (tries != ""):
    # do limited tries here
    j = 0
    for i in range(0, int(tries)):
        totry = pwgen(25)
        if pwtester(totry) != False:
            print(f"Attempt: {j} >> Okay found your password: {totry}")
            break
        else:
            j = j + 1 
            print(f"Attempt: {j} >> No match for: {totry}")

else:
    # do unlimited tries here
    def recursor():
        totry = pwgen(25)
        check = pwtester(totry)
        j = 0
        if (check == False):
            j = j + 1
            print(f"Attempt: {j} >> No match for: {totry}")
            recursor()
        else:
            print(f"Attempt: {j} >> Okay found your password: {totry}")
            return
    
    recursor()