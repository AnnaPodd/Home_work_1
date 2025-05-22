import re
from collections import Counter


def search_transactions(transactions, search_string):
    """Ищет транзакции по описанию, используя регулярные выражения."""
    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]


def count_operations_by_category(transactions, categories):
    """Подсчитывает количество операций по указанным категориям."""
    filtered_transactions = [transaction for transaction in transactions if transaction.get('category') in categories]

    descriptions = [transaction.get('description', '') for transaction in filtered_transactions]

    return dict(Counter(descriptions))