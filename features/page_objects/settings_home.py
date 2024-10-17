from appium.webdriver.common.appiumby import AppiumBy

from resources.commons.base_page import BasePage


class SettingsHome(BasePage):
    __BOTAO_SEARCH = (AppiumBy.ID, 'com.android.settings:id/search_action_bar')
    __CAMPO_SEARCH = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.google.android.settings.intelligence:id/open_search_view_edit_text"]')
    __LOCATOR_WIFI = ()

    def __init__(self):
        super().__init__()

    def clicar_no_botao_de_procurar(self):
        self._click_element(SettingsHome.__BOTAO_SEARCH)

    def enviar_wifi_para_campo_search(self):
        self._wait_and_send_keys(SettingsHome.__CAMPO_SEARCH, 'wifi')

    def validar_wifi(self):
        return True