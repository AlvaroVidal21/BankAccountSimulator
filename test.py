import random



def doing():
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
    with open("accounts.csv", "r") as file:
        lista = []
        rows = 0
        for line in file:
            rows += 1
            if rows == 1:
                continue
            else:
                data = line.strip().split(",")
                name_user = data[1]
                name_age = data[2]
                district_name = data[3].strip()
                status_district = data[4]
                balance_user = data[5]
                debt_user = data[6]

                district_name_id = dictionary_districts.get(district_name)

                lista.append(district_name_id)
                lista.append(district_name)

        print(lista)
   
                


    




if __name__ == '__main__':
    doing()