from functools import reduce

a = [1, 2, 3, 4]
n = reduce(lambda x, y: x*y, a)
b = reduce(lambda x, y: x+y, a)

print(n)
print(b)
