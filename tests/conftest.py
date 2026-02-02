import pytest
import allure
from playwright.sync_api import Page

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук, который перехватывает результат выполнения теста (passed/failed)
    и сохраняет его в атрибут item.rep_call, чтобы мы могли использовать это в фикстуре.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request, page: Page):
    """
    Фикстура, которая выполняется автоматически для каждого теста.
    После завершения теста проверяет статус. Если тест упал — делает скриншот.
    """
    yield # Здесь выполняется сам тест
    
    # Проверяем, был ли сбой в фазе вызова теста ("call")
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
