import sqlite3


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


def create_user_table(db):
    conn = sqlite3.connect(db)

    cursor = conn.cursor()

    query_create_table = """
        CREATE TABLE IF NOT EXISTS users(
            id_user INTEGER PRIMARY KEY AUTOINCREMENT,
            name_user TEXT NOT NULL,
            district_name INTEGER NOT NULL,
            balance_user REAL NOT NULL,
            debt_user REAL NOT NULL,
            status_debt TEXT NOT NULL
        )
    """

    cursor.execute(query_create_table)
    conn.commit()
    conn.close()


def insert_users(db, csv):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    query = """
        INSERT INTO users (name_user, district_name, balance_user, debt_user, status_debt) VALUES (?, ?, ?, ?, ?)
    """

    with open(csv, "r") as file:
        rows = 0
        for line in file:
            rows += 1
            if rows == 1:
                continue
            else:
                data = line.strip().split(",")
                name_user = data[0]
                district_name = data[1]
                balance_user = data[2]
                debt_user = data[3]
                status_debt = data[4]

                district_name_id = dictionary_districts.get(district_name)

                cursor.execute(query, (name_user, district_name_id, balance_user, debt_user, status_debt))

                    





    

