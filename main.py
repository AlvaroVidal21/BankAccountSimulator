from Accounts_generator.names import NAMES as nm
from Accounts_generator.accounts_generator_class import generator 
from Csv_exporter.csv_exporter import export_csv_generator as csv_exporter_func
from Accounts_generator.distritos_data import distritos_lista as dl
from database_scripts.create_db import create_db, insert_districts

import os
import pandas as pd


def doing():
    pass




if __name__ == '__main__':
    db_ruta = "db/accounts.db"
    file_csv = "./accounts.csv"

    if os.path.exists(file_csv):
        try:
            df = pd.read_csv("./accounts.csv", encoding= "utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv("./accounts.csv", encoding= "ISO-8859-1")
            print(df.head(10))
    else: 
        class_list = generator(nm)
        csv_exporter_func(class_list)

    create_db(db_ruta)
    insert_districts(db_ruta, dl)
    
    

 

    