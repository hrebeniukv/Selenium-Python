from selenium.webdriver.common.by import By

from aqa_framework.utilities.web_ui.base_page import BasePage


# from aqa_framework.utilities.web_ui.base_page import BasePage


class OrderDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __title = (By.XPATH, '//span[@class = "base"]')

    def get_order_number(self):
        order_number = self._get_element_text(self.__title)[-9::]
        return order_number
