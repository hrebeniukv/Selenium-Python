from selenium.webdriver.common.by import By
from aqa_framework.utilities.web_ui.base_page import BasePage
from aqa_framework.utilities.decorators import auto_steps


@auto_steps
class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __reset_my_password_button = (By.XPATH, '//form[contains(@class,"forget")]//div[@class="primary"]')

    def is_visible_reset_my_password_button(self):
        return self._is_visible(self.__reset_my_password_button)
