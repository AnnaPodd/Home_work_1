from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(card_type_and_number) -> str:
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
    if len(number) == 16:
        return "".join(word) + get_mask_card_number(str("".join(number)))
    else:
        return "".join(word) + get_mask_account(str("".join(number)))


print(mask_account_card("Счет 35383033474447895560"))


def get_date(original_date):
    """Функция, принимающая дату и возвращающая ее в другом формате"""
    new_date = []
    list_original_date = list(original_date)
    #for symbol in list_original_date:
    new_date.insert(0, original_date[9])
    new_date.insert(1, original_date[8])
    new_date.insert(2, original_date[-7])
    new_date.insert(3, original_date[5])
    new_date.insert(4, original_date[6])
    new_date.insert(5, original_date[-7])
    new_date.insert(6, original_date[0])
    new_date.insert(7, original_date[1])
    new_date.insert(8, original_date[2])
    new_date.insert(9, original_date[3])

    return "".join(new_date)

print(get_date("2024-03-11T02:26:18.671407"))






