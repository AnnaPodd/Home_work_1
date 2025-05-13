import json
import csv
import pandas as pd
from filter_transactions import search_transactions, count_operations_by_category


def load_transactions(file_path, file_type):
    if file_type == 'json':
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    elif file_type == 'csv':
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    elif file_type == 'xlsx':
        df = pd.read_excel(file_path)
        return df.to_dict(orient='records')


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    file_type = input(
        "Выберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла\nВведите номер: ")

    if file_type == '1':
        transactions = load_transactions('C:/Users/Анна/PycharmProjects/home_work/data/operations.json', 'json')
    elif file_type == '2':
        transactions = load_transactions('C:/Users/Анна/PycharmProjects/home_work/data/transactions.csv', 'csv')
    elif file_type == '3':
        transactions = load_transactions('C:/Users/Анна/PycharmProjects/home_work/data/transactions_excel.xlsx', 'xlsx')
    else:
        print("Неправильный выбор, программа завершена.")
        return

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").strip().upper()
        if status in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f"Операции отфильтрованы по статусу \"{status}\"")
            filtered_transactions = [t for t in transactions if t.get('state', '').upper() == status]
            break
        else:
            print(f"Статус операции \"{status}\" недоступен.")

    # Дополнительные параметры фильтрации
    sort_by_date = input("Отсортировать операции по дате? Да/Нет\n").strip().lower() == 'да'
    if sort_by_date:
        sort_order = input("Сортировать по возрастанию или по убыванию? ").strip().lower()
        filtered_transactions = sorted(filtered_transactions, key=lambda x: x['date'],
                                       reverse=(sort_order == 'по убыванию'))

    only_rub = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower() == 'да'
    if only_rub:
        filtered_transactions = [t for t in filtered_transactions if 'Руб' in t.get('currency', '')]

    filter_description = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower() == 'да'
    if filter_description:
        search_string = input("Введите строку для поиска в описании: ")
        filtered_transactions = search_transactions(filtered_transactions, search_string)

    # Вывод итогового списка транзакций
    print("Распечатываю итоговый список транзакций...")
    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(
                f"{transaction['date']} {transaction['description']}\nСчет {transaction['account']}\nСумма: {transaction['amount']} {transaction['currency']}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == '__main__':
    main()