from selenium.webdriver.common.by import By

from resources.commons.base_page import BasePage


class SeleniumHome(BasePage):
    __URL = "https://www.selenium.dev"
    __HOME_PAGE_TEXT = (By.XPATH, '')
    __DOC = (By.XPATH, '//*[@id="main_navbar"]/ul/li[3]')

    def __init__(self):
        super().__init__()

    def ir_para_selenium_home_page(self):
        self._go_to_url(SeleniumHome.__URL)

    def clicar_em_doc(self):
        self._wait_and_click_element(SeleniumHome.__DOC)

    def verificar_texto_na_home(self):
        try:
            # Aqui devemos criar uma func para validar se conseguimos encontrar o elemento __HOME_PAGE_TEXT na home page
            return True
        except:
            return False
