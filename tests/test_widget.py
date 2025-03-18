from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize("card_account, masked_account", [
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Maestro 3538303347444789", "Maestro 3538 30** **** 4789"),
    ("Visa 3538303347444", "Visa 3538 30** **** 7444")])
def test_mask_account(card_account, masked_account):
    assert mask_account_card(card_account) == masked_account


@pytest.mark.parametrize("date, correct_date", [
    ("2021-12-25T15:30:00", "25.12.2021"),
    ("2000-01-01T00:00:00", "01.01.2000"),
    ("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(date, correct_date):
    assert get_date(date) == correct_date


def test_get_date_error():
    with pytest.raises(ValueError):
        get_date("")
