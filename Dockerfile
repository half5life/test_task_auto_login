# Используем официальный образ Playwright с Python.
# Тег v1.49.0-jammy указывает на версию Playwright и версию Linux (Ubuntu Jammy).
# Это обеспечивает наличие всех системных зависимостей для браузеров.
FROM mcr.microsoft.com/playwright/python:v1.58.0-jammy

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps

COPY . .

ENV PYTHONPATH=/app

CMD ["pytest", "--alluredir=allure-results"]
