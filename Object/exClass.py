class Cal(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1+self.v2

    def substract(self):
        return self.v1-self.v2


c1 = Cal(10, 10)
print(c1.add())
print(c1.substract())
