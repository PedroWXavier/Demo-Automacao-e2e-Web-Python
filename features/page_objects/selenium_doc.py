from selenium.webdriver.common.by import By

from resources.commons.base_page import BasePage


class SeleniumDoc(BasePage):
    __BARRA_LATERAL_WEB_DRIVER = (By.ID, 'm-documentationwebdriver')
    __BARRA_LATERAL_GETTING_STARTED = (By.ID, 'm-documentationwebdrivergetting_started-li')

    def __init__(self):
        super().__init__()

    def clica_em_webdriver_na_barra_lateral(self):
        self._wait_and_click_element(SeleniumDoc.__BARRA_LATERAL_WEB_DRIVER)

    def clica_em_getting_started_na_barra_lateral(self):
        self._wait_and_click_element(SeleniumDoc.__BARRA_LATERAL_GETTING_STARTED)
