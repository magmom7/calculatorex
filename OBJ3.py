class parent_class:
    def over(self):
        print("부모 클래스의 over 메소드 입니다.")


class child_class(parent_class):
    def over(self):
        super().over()
        print("자식 클래스의 over 메소드 입니다.")


test = child_class()
test.over()
