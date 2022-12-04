from selenium.webdriver.common.by import By

from aqa_framework.page_object.syccessful_page import SuccessfulPage
from aqa_framework.utilities.web_ui.base_page import BasePage


# from aqa_framework.page_object.syccessful_page import SuccessfulPage
# from aqa_framework.utilities.web_ui.base_page import BasePage


class SummaryOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __create_order_button = (By.XPATH, '//button[contains(@class, "checkout")]')

    def click_create_order_button(self):
        self._click(self.__create_order_button)
        return SuccessfulPage(self._driver)
