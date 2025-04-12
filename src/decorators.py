def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            log_output = f"Вызов функции: {func.__name__}, аргументы: {args}, {kwargs}"
            if filename:
                with open(filename, 'a') as f:
                    f.write(f"{log_output}\n")
            else:
                print(log_output)

            try:
                result = func(*args, **kwargs)

                success_message = f"Функция: {func.__name__}, Результат: {result}"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(f"{success_message}\n")
                else:
                    print(success_message)

                return result
            except Exception as e:
                error_message = (f"Функция: {func.__name__}, "
                                 f"Ошибка: {type(e).__name__}: {e}, аргументы: {args}, {kwargs}")
                if filename:
                    with open(filename, 'a') as f:
                        f.write(f"{error_message}\n")
                else:
                    print(error_message)
                raise  # Пробрасываем исключение дальше

        return wrapper

    return decorator


@log()
def add(a, b):
    return a + b


@log()
def divide(a, b):
    return a / b
