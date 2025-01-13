import datetime
def fibonaccibucles(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
print(fibonaccibucles(6))

def fibonaccirecursiva(n):
    if n <= 1:
        return n
    else:
        return fibonaccirecursiva(n-1) + fibonaccirecursiva(n-2)
print(fibonaccirecursiva(2))


start_time = datetime.datetime.now()
fibonaccibucles(1)
end_time = datetime.datetime.now()
print("El tiempo de ejecución para n=1 bucles es:", end_time - start_time)
start_time = datetime.datetime.now()
fibonaccirecursiva(1)
end_time = datetime.datetime.now()
print("El tiempo de ejecución para n=1 recursivo es:", end_time - start_time)
start_time = datetime.datetime.now()
fibonaccibucles(10)
end_time = datetime.datetime.now()
print("El tiempo de ejecución para n=10 bucles es:", end_time - start_time)
start_time = datetime.datetime.now()
fibonaccirecursiva(10)
end_time = datetime.datetime.now()
print("El tiempo de ejecución para n=10 recursivo es:", end_time - start_time)
start_time = datetime.datetime.now()
fibonaccibucles(20)
end_time = datetime.datetime.now()
print("El tiempo de ejecución para n=20 bucles es:", end_time - start_time)
start_time = datetime.datetime.now()
fibonaccirecursiva(20)
end_time = datetime.datetime.now()
print("El tiempo de ejecución para n=20 recursivo es:", end_time - start_time)
start_time = datetime.datetime.now()
fibonaccibucles(30)
end_time = datetime.datetime.now()
print("El tiempo de ejecución para n=30 bucles es:", end_time - start_time)
start_time = datetime.datetime.now()
fibonaccirecursiva(30)
end_time = datetime.datetime.now()
print("El tiempo de ejecución para n=30 recursivo es:", end_time - start_time)
start_time = datetime.datetime.now()
fibonaccibucles(40)
end_time = datetime.datetime.now()
print("El tiempo de ejecución para n=40 bucles es:", end_time - start_time)
start_time = datetime.datetime.now()
fibonaccirecursiva(40)
end_time = datetime.datetime.now()
print("El tiempo de ejecución para n=40 recursivo es:", end_time - start_time)
