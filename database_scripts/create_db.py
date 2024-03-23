import sqlite3


def create_db(db):

    conn = sqlite3.connect(db)

    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS districts (
            id_district INTEGER PRIMARY KEY AUTOINCREMENT,
            name_district TEXT NOT NULL UNIQUE,
            status_district TEXT NOT NULL     
        )
        """)


    conn.commit()
    conn.close()


def insert_districts(db, districts_list:  list):
    # Conexión a la base de datos (suponiendo que ya tengas una base de datos SQLite creada)
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()

    query = '''
    INSERT INTO districts (name_district, status_district) VALUES (?, ?)
    '''

    for d in districts_list:
        try: 
            cursor.execute(query, (d[0], d[1]))
        except sqlite3.IntegrityError:
            pass

    conexion.commit()
    conexion.close()
