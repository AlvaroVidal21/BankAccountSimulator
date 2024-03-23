import random

dictionary_districts = {
    "San Isidro": 1,
    "Miraflores": 2,
    "Jesus Maria": 3,
    "Lince": 4,
    "Chosica": 5,
    "Chaclacayo": 6,
    "San Juan de Lurigancho": 7,
    "Cieneguilla": 8,
}

def doing():
    r = dictionary_districts["San Isidro"]
    print(r)
    print("\n")
    a = dictionary_districts.get("San Isidro")
    print(a)
   
                


    




if __name__ == '__main__':
    doing()