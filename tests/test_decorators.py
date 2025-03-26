import pytest
from src.decorators import add, divide


def test_add_success(capsys):
    result = add(3, 4)
    captured = capsys.readouterr()
    assert result == 7
    assert "Вызов функции: add, аргументы: (3, 4), {}" in captured.out
    assert "Функция: add, Результат: 7" in captured.out


def test_divide_success(capsys):
    result = divide(10, 2)
    captured = capsys.readouterr()
    assert result == 5.0
    assert "Вызов функции: divide, аргументы: (10, 2), {}" in captured.out
    assert "Функция: divide, Результат: 5.0" in captured.out


def test_divide_by_zero(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    captured = capsys.readouterr()
    assert "Функция: divide, Ошибка: ZeroDivisionError: division by zero, аргументы: (10, 0), {}" in captured.out


def test_add_string(capsys):
    with pytest.raises(TypeError):
        add("3", 4)
    captured = capsys.readouterr()
    assert "Функция: add, Ошибка: TypeError: can only concatenate str (not \"int\") to str, аргументы: ('3', 4), {}" in captured.out