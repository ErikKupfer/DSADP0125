#Target == Die wievielte Primzahl soll angezeigt werden
TargetPrimzahlen = 1000

def IsPrime(currentIteration):
    y = 2
    counter = 0
    while y < currentIteration:
        rest = currentIteration%y
        if rest == 0:
            counter = counter + 1
        y=y+1
    if counter == 0:
        global CurrentPrimzahlen
        CurrentPrimzahlen = CurrentPrimzahlen + 1

CurrentPrimzahlen = 0
iteration = 2
while CurrentPrimzahlen < TargetPrimzahlen:
    IsPrime(iteration)
    iteration=iteration+1
print(iteration-1)
