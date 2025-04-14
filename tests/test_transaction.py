import unittest
from unittest.mock import patch
import requests  # Импортируем requests
from src.transactions import calculate_transaction_amount


class TestTransaction(unittest.TestCase):

    SUPPORTED_CURRENCIES = ['RUB', 'USD', 'EUR']  # Определите поддерживаемые валюты

    @patch('requests.get')  # Замокируем requests.get
    def test_calculate_transaction_amount_rub(self, mock_get):
        transaction = {
            'operationAmount': {
                'amount': 1000,
                'currency': {'code': 'RUB'}
            }
        }
        result = calculate_transaction_amount(transaction)
        self.assertEqual(result, 1000)

    @patch('requests.get')  # Замокируем requests.get
    def test_calculate_transaction_amount_usd(self, mock_get):
        mock_get.return_value.json.return_value = {'result': 75.0}  # Предполагаемый курс USD к RUB
        mock_get.return_value.status_code = 200  # Устанавливаем статус-код ответа
        transaction = {
            'operationAmount': {
                'amount': 10,
                'currency': {'code': 'USD'}
            }
        }
        result = calculate_transaction_amount(transaction)
        self.assertEqual(result, 750.0)

    @patch('requests.get')  # Замокируем requests.get
    def test_calculate_transaction_amount_eur(self, mock_get):
        mock_get.return_value.json.return_value = {'result': 85.0}  # Предполагаемый курс EUR к RUB
        mock_get.return_value.status_code = 200  # Устанавливаем статус-код ответа
        transaction = {
            'operationAmount': {
                'amount': 10,
                'currency': {'code': 'EUR'}
            }
        }
        result = calculate_transaction_amount(transaction)
        self.assertEqual(result, 850.0)

    @patch('requests.get')  # Замокируем requests.get
    def test_calculate_transaction_amount_invalid_currency(self, mock_get):
        transaction = {
            'operationAmount': {
                'amount': 10,
                'currency': {'code': 'JPY'}  # Неподдерживаемая валюта
            }
        }
        with self.assertRaises(ValueError) as context:
            calculate_transaction_amount(transaction)
        self.assertEqual(str(context.exception), "Unsupported currency")

    @patch('requests.get')  # Замокируем requests.get
    def test_calculate_transaction_amount_api_error(self, mock_get):
        # Имитация ошибки API
        mock_get.side_effect = requests.exceptions.RequestException("Ошибка подключения")
        transaction = {
            'operationAmount': {
                'amount': 10,
                'currency': {'code': 'USD'}
            }
        }
        with self.assertRaises(RuntimeError) as context:
            calculate_transaction_amount(transaction)
        self.assertTrue("Ошибка при получении курса валют" in str(context.exception))






