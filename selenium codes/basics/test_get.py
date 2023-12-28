from selenium import webdriver


def get_url():
    driver = webdriver.chrome()
    driver.get("https://google.com")
    driver.maximize_window()
    print(driver.title)
