from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.fixture()
def length_19_digits():
    return 1234567890123456789


@pytest.fixture()
def isalpha_number():
    return "abcdefg"


def test_card_number_16_digits():
    """Проверяет маскирование 16-значного номера карты."""
    assert get_mask_card_number(1234567812345678) == "1234 56** **** 5678"


def test_card_number_15_digits():
    """Проверяет маскирование 15-значного номера карты."""
    assert get_mask_card_number(123456789012345) == "1234 56** **** 2345"


def test_card_number_13_digits():
    """Проверяет маскирование 13-значного номера карты."""
    assert get_mask_card_number(1234567890123) == "1234 56** **** 0123"


def test_card_number_19_digits(length_19_digits):
    """Проверяет маскирование 19-значного номера карты."""
    assert get_mask_card_number(length_19_digits) == "1234 56** **** 6789"


def test_no_card_number():
    """Проверяет пустой номер карты"""
    assert get_mask_card_number(""), "Введите номер карты"


def test_isalpha_card_number(isalpha_number):
    """Проверяет, как функция обрабатывает нечисловые входные данные."""
    assert get_mask_card_number(isalpha_number), "Неверный номер карты"


def test_mixed_card_number():
    """Проверяет ввод в виде строки для 16-значного номера карты."""
    assert get_mask_card_number("1234567890123456"), "1234 56** ****3456"


def test_account_number_20_digits():
    """Проверяет маскирование 20-значного номера счета."""
    assert get_mask_account(73654108430135874305) == "**4305"


def test_isalpha_account_number(isalpha_number):
    assert get_mask_account(isalpha_number), "Неверный номер счета"


def test_account_number_19_digits(length_19_digits):
    """Проверяет 19-значный номер счета(неверный)."""
    assert get_mask_account(length_19_digits), "Неверная длина счета"


def test_account_number_21_digits():
    """Проверяет 21-значный номер счета(неверный)."""
    assert get_mask_account(123456789012345678901), "Неверная длина счета"
