import random



class a:
    def __init__(self, name):
        self.name = name
        self._jaja = 0
        self.__test = None

    @property
    def test(self):
        return self.__test
    
    @test.setter
    def test(self, value):
        self.__test = value
        self._jaja = random.randint(0, 100)

    
        





def doing():
    ac = a("alva")

    print(f"""
    {ac.name}
    {ac.jaja}
    """)

    print("....")
    ac.test = 10

    print(f"""
    {ac.name}
    {ac.jaja}
    """)





if __name__ == '__main__':
    doing()