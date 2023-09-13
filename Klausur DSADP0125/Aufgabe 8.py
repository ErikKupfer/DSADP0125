#Aufgabe 8 Klausur

def CalculateFibonacci(index):                          

    fibonacci = ['']*(index+1)                          

    fibonacci[0] = 1                                    
    fibonacci[1] = 1                                    

    for k in range(2,index+1):
        fibonacci[k] = fibonacci[k-1] + fibonacci[k-2]  

    return(fibonacci[index-1])                          

fibonacciNumber = 115     

number = CalculateFibonacci(fibonacciNumber-1)
print (f"Fibonacci Zahl #{fibonacciNumber}:" , number)
