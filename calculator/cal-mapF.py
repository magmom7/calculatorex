
num1, num2 = map(int, input("두수를 입력하세요 ").split())

op = input("계산할 연산자를 입력하세요 ")

if op == '+':
    print(f'{num1}{op}{num2}={num1+num2}입니다.')
elif op == '-':
    print(f'{num1}{op}{num2}={num1-num2}입니다.')
elif op == '*':
    print(f'{num1}{op}{num2}={num1*num2}입니다.')
elif op == '/':
    print(f'{num1}{op}{num2}={num1/num2}입니다.')
elif op == '%':
    print(f'{num1}{op}{num2}={num1%num2}입니다.')
else:
    print("알 수 없는 연산자 입니다.")
