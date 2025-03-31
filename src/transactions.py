from src.external_api import get_exchange_rate


def calculate_transaction_amount(transaction):
    """Возвращает сумму транзакции в рублях."""
    amount = transaction['amount']
    currency = transaction['currency']

    if currency == 'RUB':
        return float(amount)

    exchange_rate = get_exchange_rate(currency)
    return float(amount) * exchange_rate