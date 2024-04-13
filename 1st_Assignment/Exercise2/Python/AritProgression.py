# an = a1 + (n-1)r
def aritmeticProgression(n, u, r):
   list = []
   for i in range(1 , n + 1):
      list.append(u + (i - 1) * r)
   return list

print(aritmeticProgression(5, 1, 2))