# 부모 클래스
class parent_class:
    def parent_print(self):
        print('부모 클래스 입니다.')

    def add(self, a, b):
        print('{0} + {1} = {2} 입니다.'.format(a, b, a + b))

# 부모 클래스를 parent_class 으로 지정


class child_class(parent_class):
    def child_print(self):
        print('자식 클래스 입니다.')


# 자식 클래스인 child_class의 인스턴스 생성
test = child_class()


# 자식 클래스인 child_class 클래스의 child_print 호출
test.child_print()

# 부모 클래스인 parent_class 클래스의 parent_print 호출
test.parent_print()

# 부모 클래스인 parent_class 클래스의 add 호출
test.add(5, 6)
