


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



