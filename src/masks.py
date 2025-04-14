import logging


utils_logger = logging.getLogger('masks')
utils_logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler('C:\\Users\\Анна\\PycharmProjects\\home_work\\logs\\masks.log',
                                   mode='a')
file_handler.setLevel(logging.DEBUG)  # Уровень обработчика


file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)


utils_logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | str) -> str:
    """Функция, маскирующая номер карты"""
    str_card_number = str(card_number)
    if len(str_card_number) < 13 or len(str_card_number) > 19:
        utils_logger.error("Неверная длина номера карты: %s", str_card_number)  # Логирование ошибки
        return "Неверная длина номера карты"

    masked_number = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
    utils_logger.info("Маскированный номер карты: %s", masked_number)  # Логирование успешного результата
    return masked_number


def get_mask_account(account_number: int | str) -> str:
    """Функция, маскирующая номер счета"""
    str_account_number = str(account_number)
    if len(str_account_number) != 20:
        utils_logger.error("Неверная длина номера счета: %s", str_account_number)  # Логирование ошибки
        return "Неверная длина номера счета"

    masked_account = f"**{str_account_number[-4:]}"
    utils_logger.info("Маскированный номер счета: %s", masked_account)  # Логирование успешного результата
    return masked_account


print(get_mask_card_number(1234567890123456))
print(get_mask_account(73654108430135874305))
