class Windows:
    os = "window10"		# 클래스 속성

    def __init__(self):
        self.out = "OS: " + self.os

    @staticmethod
    def static_os():
        return Windows()

    @classmethod
    def class_os(cls):
        return cls()

    def os_output(self):
        print(self.out)


class Linux(Windows):
    os = "Linux"		# 클래스 속성


a = Linux.static_os()
a.os_output()

b = Linux.class_os()
b.os_output()
