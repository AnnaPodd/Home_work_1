from src.external_api import get_exchange_rate

def calculate_transaction_amount(transaction):
    """Возвращает сумму транзакции в рублях."""
    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['code']

    # Проверяем, поддерживается ли валюта
    if currency not in ['RUB', 'USD', 'EUR']:
        raise ValueError("Unsupported currency")

    if currency == 'RUB':
        return float(amount)

    try:
        exchange_rate = get_exchange_rate(currency)
        return float(amount) * exchange_rate
    except Exception:
        raise RuntimeError("Ошибка при получении курса валют")
