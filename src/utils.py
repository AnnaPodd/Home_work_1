import json
import os
import logging


logging.basicConfig(level=logging.INFO)

def load_json(json_file_path):
    """Загружает данные из JSON-файла и проверяет формат данных."""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                return data
            else:
                logging.warning("Данные в файле не являются списком.")
    except FileNotFoundError:
        logging.error(f"Файл {json_file_path} не найден.")
    except json.JSONDecodeError:
        logging.error("Ошибка при декодировании JSON.")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
    return []  # Возвращает пустой список в случае ошибки

def main():
    """Получает путь к директории, где находится этот файл"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_dir, '..', 'data', 'operations.json')

    # Проверка наличия директории 'data'
    if not os.path.exists(os.path.join(current_dir, '..', 'data')):
        os.makedirs(os.path.join(current_dir, '..', 'data'))
        logging.info("Создана директория 'data'.")

    # Проверка существования файла и его загрузка
    data = load_json(json_file_path)
    if data:
        print("Загруженные данные:")
        print(data)
    else:
        print("Данные не загружены или файл пуст.")

if __name__ == "__main__":
    main()