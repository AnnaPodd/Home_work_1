from src.processing import filter_by_state, sort_by_date
import pytest


@pytest.fixture()
def operation_input():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_filter_by_state_ascending(operation_input):
    executed_operations = filter_by_state(operation_input, state="EXECUTED")
    expected_executed = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert executed_operations == expected_executed, "Ошибка сортировки"


def test_filter_by_state_descending(operation_input):
    canceled_operations = filter_by_state(operation_input, state="CANCELED")
    expected_canceled = [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    assert canceled_operations == expected_canceled, "Ошибка сортировки"


def test_filter_state_incorrect_state(operation_input):
    incorrect_operations = filter_by_state(operation_input, state="ANOTHER")
    expected_incorrect = []
    assert incorrect_operations == expected_incorrect, "Неверный статус"


def test_no_state():
    assert [{'id': 41428829, 'state': 'STATUS', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': '', 'STATUS': '2018-06-30T02:08:58.425572'}], "Неверный статус"


def test_sort_by_date_ascending(operation_input):
    true_operations = sort_by_date(operation_input, reverse=True)
    expected_true = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert true_operations == expected_true


def test_sort_by_date_descending(operation_input):
    false_operations = sort_by_date(operation_input, reverse=False)
    expected_false = [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                      {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    assert false_operations == expected_false
