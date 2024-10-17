from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Driver:
    __driver = None

    @classmethod
    def get_driver(cls) -> WebDriver:
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
        return cls.__driver

    @classmethod
    def quit(cls):
        cls.__driver.quit()
        cls.__driver = None
