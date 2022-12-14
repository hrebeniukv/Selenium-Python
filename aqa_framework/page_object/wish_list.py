from selenium.webdriver.common.by import By
from aqa_framework.utilities.web_ui.base_page import BasePage
from aqa_framework.utilities.decorators import auto_steps


@auto_steps
class WishList(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __actual_wish_list_button = (By.XPATH, '//button[@class="action update"]')

    def is_visible_button(self):
        return self._is_visible(self.__actual_wish_list_button)
