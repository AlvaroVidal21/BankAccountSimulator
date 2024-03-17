import random
from distritos import DISTRITOS_STATUS as ds
from names import NAMES as nm



class AccountBank:
    def __init__(self, name):
        self.name = name
        self._district = None
        self._district_status = None
        self._age = 0
        self.__balance = 0
        self.__debt = 0
        self._status_debt = None # "normal", "peligro", "muy peligroso"


    def get_district(self):
        random_district = random.choice(ds)
        self._district = random_district[0]
        self._district_status = random_district[1]

    def get_age(self):
        self._age = random.randint(18, 50)

    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        status = self._district_status
        age = self._age
        r_ = random.random()
 
        # STATUS A
        if status == 'A':
            if age >= 45:
                if r_ <= 0.85:
                    self.__balance = value * random.randint(10000, 30000)
                elif r_ > 0.85 and r_ <= 0.95:
                    self.__balance = value * random.randint(3000, 10000)
                else:
                    self.__balance = value * random.randint(500, 3000)
            elif age >= 30 and age < 45:
                if r_ <= 0.85:
                    self.__balance = value * random.randint(3000, 10000)
                elif r_ > 0.85 and r_ <= 0.95:
                    self.__balance = value * random.randint(500, 3000)
                else:
                    self.__balance = value * random.randint(10000, 20000)
            else:
                if r_ <= 0.85:
                    self.__balance = value * random.randint(500, 3000)
                else:
                    self.__balance = value * random.randint(3000, 10000)
        
        # STATUS B
        elif status == 'B':
            if age >= 45:
                if r_ <= 0.85:
                    self.__balance = value * random.randint(5000, 15000)
                elif r_ > 0.85 and r_ <= 0.95:
                    self.__balance = value * random.randint(1500, 5000)
                else:
                    self.__balance = value * random.randint(300, 1500)
            elif age >= 30 and age < 45:
                if r_ <= 0.85:
                    self.__balance = value * random.randint(1500, 5000)
                elif r_ > 0.85 and r_ <= 0.95:
                    self.__balance = value * random.randint(300, 1500)
                else:
                    self.__balance = value * random.randint(5000, 10000)
            else:
                if r_ <= 0.85:
                    self.__balance = value * random.randint(300, 1500)
                else:
                    self.__balance = value * random.randint(1500, 5000)
        
        # STATUS C
        elif status == 'C':
            if age >= 45:
                if r_ <= 0.85:
                    self.__balance = value * random.randint(1000, 5000)
                elif r_ > 0.85 and r_ <= 0.95:
                    self.__balance = value * random.randint(300, 1000)
                else:
                    self.__balance = value * random.randint(100, 300)
            elif age >= 30 and age < 45:
                if r_ <= 0.85:
                    self.__balance = value * random.randint(300, 1000)
                elif r_ > 0.85 and r_ <= 0.95:
                    self.__balance = value * random.randint(100, 300)
                else:
                    self.__balance = value * random.randint(1000, 2000)
            else:
                if r_ <= 0.85:
                    self.__balance = value * random.randint(100, 300)
                else:
                    self.__balance = value * random.randint(300, 1000)

        # STATUS D
        else:
            if age >= 45:
                if r_ <= 0.85:
                    self.__balance = value * random.randint(100, 500)
                elif r_ > 0.85 and r_ <= 0.95:
                    self.__balance = value * random.randint(30, 100)
                else:
                    self.__balance = value * random.randint(10, 30)
            elif age >= 30 and age < 45:
                if r_ <= 0.85:
                    self.__balance = value * random.randint(30, 100)
                elif r_ > 0.85 and r_ <= 0.95:
                    self.__balance = value * random.randint(10, 30)
                else:
                    self.__balance = value * random.randint(100, 200)
            else:
                if r_ <= 0.85:
                    self.__balance = value * random.randint(10, 30)
                else:
                    self.__balance = value * random.randint(30, 100)


    @property
    def debt(self):
        return self.__debt
    
    @debt.setter
    def debt(self, value):
        r_ = random.random()      

        if r_ <= 0.85:
            self.__debt = value * (self.__balance * (random.randint(1, 50)/ 100))
            self._status_debt = "normal"

        elif r_ > 0.85 and r_ <= 0.95:
            self.__debt = value * (self.__balance * (random.randint(51, 65)/ 100))
            self._status_debt = "peligro"

        else:
            self.__debt = value * (self.__balance * (random.randint(66, 85)/ 100))
            self._status_debt = "muy peligroso"

def generator(names: list) -> list:
    accounts = []
    count = 1
    for name in names:
        if count <= 9:
            acc = 'ac' + '00' + str(count)
        else:
            acc = 'ac' + '0' + str(count)

        acc = AccountBank(name)
        acc.get_district()
        acc.get_age()
        acc.balance = 1
        acc.debt = 1
        accounts.append(acc)

    return accounts
    

        




def doing():
    lista = generator(nm)

    for i in lista:
        print(f"""
        Nombre: {i.name}
        Distrito: {i._district}
        Estatus del distrito: {i._district_status}
        Edad: {i._age}
        Saldo: {i.balance}
        Deuda {i.debt}
        \n
        """)




if __name__ == '__main__':
    doing()
    

