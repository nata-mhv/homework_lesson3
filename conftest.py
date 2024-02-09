from selene import browser, be, have
import pytest

@pytest.fixture(scope='session')
def browser_open():
    browser.open('https://google.com')
    print("Browser opens")

    yield

    print("Browser is closed")