import json
import os
import logging
from src.config import LOG_DIR, file_formatter


utils_logger = logging.getLogger('utils')
utils_logger.setLevel(logging.DEBUG)


utils_file_handler = logging.FileHandler(LOG_DIR / 'utils.log', mode='a')
utils_file_handler.setLevel(logging.DEBUG)


utils_file_handler.setFormatter(file_formatter)
utils_logger.addHandler(utils_file_handler)
utils_logger.addHandler(utils_file_handler)


def load_json(json_file_path):
    """Загружает данные из JSON-файла и проверяет формат данных."""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                utils_logger.info("Успешно загружены данные из '%s'.", json_file_path)  # Логирование успешной загрузки
                return data
            else:
                utils_logger.warning("Данные в файле '%s' не являются списком.", json_file_path)
    except FileNotFoundError:
        utils_logger.error("Файл '%s' не найден.", json_file_path)
    except json.JSONDecodeError:
        utils_logger.error("Ошибка при декодировании JSON в файле '%s'.", json_file_path)
    except Exception as e:
        utils_logger.error("Произошла ошибка (%s): %s", type(e).__name__, e)
    return []  # Возвращает пустой список в случае ошибки


def main():
    """Получает путь к директории, где находится этот файл и загружает данные."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_dir, '..', 'data', 'operations.json')

    # Проверка наличия директории 'data'
    if not os.path.exists(os.path.join(current_dir, '..', 'data')):
        os.makedirs(os.path.join(current_dir, '..', 'data'))
        utils_logger.info("Создана директория 'data'.")  # Логирование создания директории

    # Проверка существования файла и его загрузка
    data = load_json(json_file_path)
    if data:
        print("Загруженные данные:")
        print(data)
    else:
        print("Данные не загружены или файл пуст.")


if __name__ == "__main__":
    main()
