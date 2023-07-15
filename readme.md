# Пример тестирования gRPC

**Установка**
- Необходим Python >= 3.9


```
git clone https://github.com/SeniorK0tik/gRPCTesting
pip install poetry
poetry self add 'poethepoet[poetry_plugin]'
poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
```

**Запуск тестов**
- Запуск сервера
```
poetry poe start_server
```

- Запуск тестов
 ```
poetry poe start_tests
```

**Запуск allure**
- Необходимо установить allure локально

```
allure serve
or
allure generate
```
Комментарий:
- Данный проэкт является простым примером запуска сервера с использование .proto файла и запуском клиента, который слушает и получается обновления