# Test Task Auto Login (Saucedemo)

Автоматизация тестирования логина на сайте [saucedemo.com](https://www.saucedemo.com/) с использованием Python + Playwright + Allure.

## Структура проекта
- `pages/` - Page Object модели.
- `tests/` - Тестовые сценарии.
- `data/` - Тестовые данные.

## Установка и запуск
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
2. Запуск тестов:
   ```bash
   python -m pytest
   ```

## Allure отчеты
1. Запуск тестов с генерацией данных для Allure:
   ```bash
   python -m pytest --alluredir=allure-results
   ```
2. Просмотр отчета в браузере (требуется установленный [Allure commandline](https://allurereport.org/docs/v2/install/)):
   ```bash
   allure serve allure-results
   ```
