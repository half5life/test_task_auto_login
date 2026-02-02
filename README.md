# Test Task Auto Login (Saucedemo)

Проект по автоматизации тестирования формы логина на сайте [saucedemo.com](https://www.saucedemo.com/).
Реализовано с использованием **Python 3.10**, **Playwright**, **Pytest** и паттерна **Page Object Model**.

## Требования
- Python 3.10+
- Docker (для запуска тестов в изолированном контейнере)

## Установка (Локально)

1. **Клонируйте репозиторий**

2. **Создайте и активируйте виртуальное окружение:**
   - Windows:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Linux/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

## Запуск тестов

### 1. Локальный запуск
Запуск всех тестов:
```bash
pytest
```

Запуск с генерацией отчета Allure:
```bash
pytest --alluredir=allure-results
```

### 2. Запуск в Docker
Если у вас установлен Docker, вы можете запустить тесты в изолированном контейнере без установки зависимостей локально.

**Способ А: Используя скрипт (Windows PowerShell)**
Просто запустите файл скрипта:
```powershell
.\run_tests.ps1
```

**Способ Б: Вручную (Любая ОС)**
1. Соберите образ:
   ```bash
   docker build -t saucedemo-tests .
   ```
2. Запустите контейнер:
   ```bash
   # Windows (PowerShell)
   docker run --rm -v ${PWD}/allure-results:/app/allure-results saucedemo-tests

   # Linux/macOS
   docker run --rm -v $(pwd)/allure-results:/app/allure-results saucedemo-tests
   ```

## Просмотр отчета Allure
После прогона тестов (локально или в Docker), в папке `allure-results` появятся файлы с результатами.
Чтобы посмотреть красивый HTML отчет, выполните команду (требуется установленный [Allure CLI](https://allurereport.org/docs/install/)):

```bash
allure serve allure-results
```