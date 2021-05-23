lst = ['a', 'b', 'hi', 'hh']
a = (1, 2, 3, 4)
b = [100, 200, 300, 400]
# t = zip(lst, a, b)
# print(list(t))   패킹하는 과정


z, x, c = zip(*t)   튜플을 언패킹 하는 과정
print(z, x, c)
