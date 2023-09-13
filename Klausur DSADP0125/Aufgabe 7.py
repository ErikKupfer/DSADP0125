#Aufgabe 7 Klausur

testList = [4, 16, 25, 12, 6, 15, 10, 13, 0, 1, 2, 26, 17, 5, 19, 3, 23, 22, 8, 14, 21, 24, 9, 11, 18, 7, 20]
    
size = len(testList)
    
for ind in range(size):
    min_index = ind
    for j in range(ind + 1, size):
        if testList[j] < testList[min_index]:
            min_index = j
                
    testList[ind], testList[min_index] = testList[min_index], testList[ind]

print(testList)
