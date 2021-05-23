from functools import reduce

n = int(input("1부터 어디까지 더할까여? "))
lst = list(range(n+1))
lst = reduce(lambda a, b: a+b, lst)

print(f'{lst}입니다.')
