import csv
import pandas as pd


def load_csv(file_path, delimiter=','):
    """Загружает данные из CSV файла и возвращает список словарей."""
    try:
        data = pd.read_csv(file_path, delimiter=delimiter)
        return data.to_dict(orient='records')  # Преобразует в список словарей
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{file_path}' не найден.")
    except Exception as e:
        raise Exception(f"Ошибка при загрузке CSV: {e}")


def load_xlsx(file_path):
    """Загружает данные из XLSX файла и возвращает список словарей."""
    try:
        data = pd.read_excel(file_path)
        return data.to_dict(orient='records')  # Преобразует в список словарей
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{file_path}' не найден.")
    except Exception as e:
        raise Exception(f"Ошибка при загрузке XLSX: {e}")