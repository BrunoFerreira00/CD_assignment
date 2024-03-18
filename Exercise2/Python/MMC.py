def mmc(a,b):
    total = a if a > b else b
    while(True):
        if(total % a == 0 and total % b == 0):
            return total
        total += 1


print(mmc(136,255)) # 20