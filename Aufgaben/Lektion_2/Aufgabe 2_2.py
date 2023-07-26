import random

stackSize = 50
stack = [] #für rechts verschiebung
stack2 = [] #für links verschiebung

for i in range(0,stackSize):
    randomNumber = random.randint(0,1000)
    stack.append(randomNumber)
    stack2.append(randomNumber)


print(stack)

#rechts verschiebung
for i in range(0,25):
    stack.insert(0,"0")
    stack.pop(50)
    print(stack)
print("\n")

#links verschiebung
print (stack2)
for i in range(0,25):
    stack2.insert(50,"0")
    stack2.pop(0)
    print(stack2)
