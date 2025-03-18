 # Проект Д/З

 - ## Описание:
   Д/З - проект для работы с банковскими операциями.

 - ## Установка:
   1. Клонируйте репозиторий:
   git clone https://github.com/AnnaPodd/Home_work_1.git
   2. Установите зависимости:
   pip install -r requirements.txt
   3. Создайте базу данных и выполните миграции:
   python manage.py migrate
   4. Запустите локальный сервер:
   python manage.py runserver
 
 - ## Тестирование:
   1. Для тестирования проекта используется библиотека `pytest`. Чтобы запустить тесты, выполните команду:
      pytest
   2. Тесты покрывают следующие модули и функции:
      - `masks`: функции `get_mask_card_number` и `get_mask_account`.
      - `widget`: функции `mask_account_card` и `get_date`.
      - `processing`: функции `filter_by_state` и `sort_by_date`. 
   3. Покрытие тестами составляет 100% кода проекта.

   
   
