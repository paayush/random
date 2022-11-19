import random

def RemoveDublicate(randNum):
    res = []
    for num in randNum:
        if num not in res:
            res.append(num)
    return res

def GenerateRand(start, end, count):
    res = []

    for j in range(count):
        res.append(random.randint(start, end))

    return res

randomNumber = GenerateRand(10, 20, 7)
result = RemoveDublicate(randomNumber)
print(result)

