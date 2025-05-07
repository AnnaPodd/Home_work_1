import os

from finance_reader import load_csv, load_xlsx


def finance_loader():
    csv_file_path = "data/transactions.csv"
    xlsx_file_path = "data/transactions_excel.xlsx"

    print(f"Текущий рабочий каталог: {os.getcwd()}")

    try:
        csv_data = load_csv(csv_file_path)
        print("Данные из CSV:")
        print(csv_data)
    except FileNotFoundError as e:
        print(f"Ошибка: Файл CSV не найден. {e}")
    except Exception as e:
        print(f"Ошибка при загрузке CSV: {e}")

    try:
        xlsx_data = load_xlsx(xlsx_file_path)
        print("Данные из XLSX:")
        print(xlsx_data)
    except FileNotFoundError as e:
        print(f"Ошибка: Файл XLSX не найден. {e}")
    except Exception as e:
        print(f"Ошибка при загрузке XLSX: {e}")


if __name__ == "__main__":
    finance_loader()
