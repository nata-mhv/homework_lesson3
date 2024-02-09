from selenium.webdriver import Chrome, ChromeOptions

def test_size():
    opts = ChromeOptions()
    opts.add_argument("--window-size=1060,600")

    driver = Chrome(options=opts)
    print("Size changed")