import re
from collections import Counter


def search_transactions(transactions, search_string):
    """Ищет транзакции по описанию, используя регулярные выражения."""
    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]


def count_operations_by_category(transactions):
    """Подсчитывает количество операций по категориям."""
    descriptions = [transaction.get('description', '') for transaction in transactions]
    return dict(Counter(descriptions))