
@pytest.fixture(scope='function')
def setting_browser():
    browser.config.window_height = 700
    browser.config.window_width = 1200
    print('Browser opens')

    yield

    browser.quit()
    print('Browser is closed')