import logging
from src.config import LOG_DIR, file_formatter


logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)


masks_file_handler = logging.FileHandler(LOG_DIR / 'masks.log', mode='a')
masks_file_handler.setLevel(logging.DEBUG)
masks_file_handler.setFormatter(file_formatter)
logger.addHandler(masks_file_handler)


def get_mask_card_number(card_number: int | str) -> str:
    """Функция, маскирующая номер карты"""
    str_card_number = str(card_number)
    if len(str_card_number) < 13 or len(str_card_number) > 19:
        logger.error("Неверная длина номера карты: %s", str_card_number)  # Логирование ошибки
        return "Неверная длина номера карты"

    masked_number = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
    logger.info("Маскированный номер карты: %s", masked_number)  # Логирование успешного результата
    return masked_number


def get_mask_account(account_number: int | str) -> str:
    """Функция, маскирующая номер счета"""
    str_account_number = str(account_number)
    if len(str_account_number) != 20:
        logger.error("Неверная длина номера счета: %s", str_account_number)  # Логирование ошибки
        return "Неверная длина номера счета"

    masked_account = f"**{str_account_number[-4:]}"
    logger.info("Маскированный номер счета: %s", masked_account)  # Логирование успешного результата
    return masked_account


print(get_mask_card_number(1234567890123456))
print(get_mask_account(73654108430135874305))
