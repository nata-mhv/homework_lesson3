from selene import browser, be, have

def test_search(setting_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    print('Search is fulfilled')

def test_incorrect_search(setting_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('ehfrubgv').press_enter()
    browser.element('[id="search"]').should(have.text('Your search - ehfrubgv - did not match any documents.'))
    print('Search is fulfilled. Nothing is found')