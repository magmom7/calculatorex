n = int(input("숫자를 입력 "))
a = list(range(n))
b = filter(lambda number: number % 2 == 0, a)
print(list(b))
