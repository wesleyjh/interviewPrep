
def primeNumberChecker(x):
    if x > 1:
        for i in range(2, int(x/2)+1):
            if x%i == 0:
                return False
        return True
    return False

def makePrimeList(x):
    primeNumberList = []
    for i in range(x):
        if primeNumberChecker(i):
            primeNumberList.append(i)
    return primeNumberList

print(primeNumberChecker(21), 21)
print(makePrimeList(100))