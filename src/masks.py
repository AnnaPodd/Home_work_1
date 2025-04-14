def get_mask_card_number(card_number: int | str) -> str:
    """Функция, маскирующая номер карты"""
    str_card_number = str(card_number)
    if len(str_card_number) < 13 or len(str_card_number) > 19:
        return "Неверная длина номера карты"
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account_number: int | str) -> str:
    """Функция, маскирующая номер счета"""
    str_account_number = str(account_number)
    if len(str_account_number) != 20:
        return "Неверная длина номера счета"
    return f"**{str_account_number[-4:]}"


print(get_mask_card_number(1234567890123456))
print(get_mask_account(73654108430135874305))
