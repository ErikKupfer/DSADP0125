#Aufgabe 6 Klausur

import random

upperLimit = 26
stackSize = upperLimit+1
stack = []

while len(stack) < stackSize:
    randomNumber = random.randint(0, upperLimit)
    if randomNumber not in stack:
        stack.append(randomNumber)

print(stack)
