from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(card_type_and_number: str) -> str:
    """Функция, маскирующая название карты и ее номер или счет"""
    str_card_type_and_number = str(card_type_and_number)
    word = []
    number = []
    for symbol in str_card_type_and_number:
        if symbol.isalpha():
            word.append(symbol)
        if symbol == " ":
            word.append(symbol)
        if symbol.isdigit():
            number.append(symbol)
    if 13 <= len(number) <= 19:
        return "".join(word) + get_mask_card_number(str("".join(number)))
    else:
        return "".join(word) + get_mask_account(str("".join(number)))


print(mask_account_card("Счет 35383033474445555666"))


def get_date(original_date: str) -> str:
    """Функция, принимающая дату и возвращающая ее в формате DD.MM.YYYY."""
    date_part = original_date.split('T')[0]
    year, month, day = date_part.split('-')
    new_date = f"{day}.{month}.{year}"
    return new_date


print(get_date("2024-03-11T02:26:18.671407"))
