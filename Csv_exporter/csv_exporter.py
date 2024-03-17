# exportamos el generador de cuentas
from ..Accounts_generator.accounts_generator_class import generator  # Genera una lista (50) de objetos de la clase Account
# from names import NAMES as nm
from ..Accounts_generator.names import NAMES as nm

account_list = generator(nm)


def export_csv_generator(account_list: list) -> None:
    """
    Exporta la lista de cuentas generadas a un archivo .csv
    """
    id = 1
    with open("accounts.csv", "w") as file:
        file.write("id, name, age, district, status_district, balance, debt, status_debt\n")
        for account in account_list:
            file.write(f"{id}, {account.name}, {account._age}, {account._district}, {account._district_status}, {account.balance}, {account.debt}, {account._status_debt}\n")
            id += 1



if __name__ == '__main__':
    export_csv_generator(account_list)
    print("Archivo 'accounts.csv' creado con éxito")