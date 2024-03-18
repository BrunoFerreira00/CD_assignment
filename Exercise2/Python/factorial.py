def factorial(num):
    total = 1
    while(num > 0):
        total *= num
        num -= 1
    return total

print(factorial(5)) # 120