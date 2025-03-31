import unittest
from unittest.mock import patch
from src.transactions import calculate_transaction_amount


class TestTransaction(unittest.TestCase):

    @patch('external_api.get_exchange_rate')
    def test_calculate_transaction_amount_rub(self, mock_get_exchange_rate):
        transaction = {'amount': 1000, 'currency': 'RUB'}
        result = calculate_transaction_amount(transaction)

        self.assertEqual(result, 1000)

    @patch('external_api.get_exchange_rate')
    def test_calculate_transaction_amount_usd(self, mock_get_exchange_rate):
        mock_get_exchange_rate.return_value = 75.0  # Предполагаемый курс USD к RUB
        transaction = {'amount': 10, 'currency': 'USD'}
        result = calculate_transaction_amount(transaction)

        self.assertEqual(result, 750.0)

    @patch('external_api.get_exchange_rate')
    def test_calculate_transaction_amount_eur(self, mock_get_exchange_rate):
        mock_get_exchange_rate.return_value = 85.0  # Предполагаемый курс EUR к RUB
        transaction = {'amount': 10, 'currency': 'EUR'}
        result = calculate_transaction_amount(transaction)

        self.assertEqual(result, 850.0)


if __name__ == '__main__':
    unittest.main()