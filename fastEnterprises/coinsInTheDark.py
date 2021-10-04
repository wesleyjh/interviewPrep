from random import randint

def createCoins():
    coinList = []
    for i in range(10):
        coinList.insert(randint(0, 25), "H")
    for i in range (16):
        coinList.insert(randint(0, 25), "T")
    return coinList

def flipCoins(arr):
    newArr = []
    for i in range(len(arr)):
        if arr[i] == "H":
            newArr.append("T")
        elif arr[i] == "T":
            newArr.append("H")
    return newArr

def showWork(headsNum):
    coinList = createCoins()
    headsList = coinList[0:headsNum]
    tailsList = coinList[headsNum:]
    print(headsList)
    print(flipCoins(headsList))

showWork(10)