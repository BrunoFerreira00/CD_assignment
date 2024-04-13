def primal(left,right):
    list = []
    nextNum = left
    while nextNum <= right:
        if isPrime(nextNum):
            list.append(nextNum)
        nextNum += 1
    return list

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(primal(10,20))
