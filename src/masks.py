def get_mask_card_number(card_number):
    """Функция, маскирующая номер карты"""
    str_card_number = str(card_number)
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account_number):
    """Функция, маскирующая номер счета"""
    str_account_number = str(account_number)
    return f"**{str_account_number[-4:]}"


#print(get_mask_card_number(1234567890123456))
#print(get_mask_account(73654108430135874305))







