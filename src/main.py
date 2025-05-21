import json
import os
import csv
import pandas as pd
from filter_transactions import search_transactions

os.chdir('C:/Users/Анна/PycharmProjects/home_work')


def load_transactions(file_path, file_type):
    if file_type == 'json':
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else [data]
    elif file_type == 'csv':
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            return list(reader)
    elif file_type == 'xlsx':
        df = pd.read_excel(file_path)
        return df.to_dict(orient='records')


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    file_choice = input(
        "Выберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\nВведите номер: ")

    if file_choice == '1':
        transactions = load_transactions('data/operations.json', 'json')
    elif file_choice == '2':
        transactions = load_transactions('data/transactions.csv', 'csv')
    elif file_choice == '3':
        transactions = load_transactions('data/transactions_excel.xlsx', 'xlsx')
    else:
        print("Неправильный выбор, программа завершена.")
        return

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\n").strip().upper()
        if status in ['EXECUTED', 'CANCELED', 'PENDING']:
            filtered_transactions = [t for t in transactions if isinstance(t.get('state'), str) and t['state'].upper() == status]
            print(f"Операции отфильтрованы по статусу \"{status}\"")
            break
        else:
            print(f"Статус операции \"{status}\" недоступен.")

    sort_by_date = input("Отсортировать операции по дате? Да/Нет\n").strip().lower() == 'да'
    if sort_by_date:
        sort_order = input("Сортировать по возрастанию или по убыванию? ").strip().lower()
        filtered_transactions = sorted(
            filtered_transactions,
            key=lambda x: x['date'],
            reverse=(sort_order == 'по убыванию')
        )

    filter_description = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower() == 'да'
    if filter_description:
        search_string = input("Введите строку для поиска в описании: ")
        filtered_transactions = search_transactions(filtered_transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            if isinstance(transaction, dict):
                # Обработаем данные в зависимости от формата входных файлов
                date = transaction.get('date', 'Дата не указана')
                description = transaction.get('description', 'Описание не указано')
                amount = transaction.get('amount', 'Сумма не указана')

                if 'operationAmount' in transaction:  # Для JSON
                    amount = transaction['operationAmount']['amount']
                    currency = transaction['operationAmount']['currency']['name']
                    from_account = transaction.get('from', 'Счет не указан')
                    to_account = transaction.get('to', 'Счет не указан')
                else:  # Для CSV и Excel
                    currency = transaction.get('currency_name', '')
                    from_account = transaction.get('from', 'Счет не указан')
                    to_account = transaction.get('to', 'Счет не указан')

                print(f"{date} {description}")
                print(f"Счет {from_account} -> Счет {to_account}")
                print(f"Сумма: {amount} {currency}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == '__main__':
    main()