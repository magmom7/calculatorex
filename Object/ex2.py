class fight:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def print_name(self):
        print(self.name)

    def attack1(self, oppo):
        print(f"{self.attack * 10}만큼 상대방을 공격했습니다!")
        oppo.health -= self.attack * 10
        print("상대의 체력은 ", oppo.health, "가 되었습니다!")


a = fight("내가", 100, 1)
b = fight("너의", 10, 2)
a.attack1(b)
