from selenium.webdriver.common.by import By

from aqa_framework.utilities.feke_data import FakeData
from aqa_framework.utilities.web_ui.base_page import BasePage


# from aqa_framework.utilities.feke_data import FakeData
#
# from aqa_framework.utilities.web_ui.base_page import BasePage


class AddressDataPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __first_name_input = (By.XPATH, '//input[@name = "firstname"]')
    __last_name_input = (By.XPATH, '//input[@name = "lastname"]')
    __phone_number_input = (By.XPATH, '//input[@name = "telephone"]')
    __address_input = (By.XPATH, '//input[@name = "street[0]"]')
    __country_drop_down = (By.XPATH, '//select[@name = "country_id"]')
    __region_drop_down = (By.XPATH, '//select[@name = "region_id"]')
    __city_input = (By.XPATH, '//input[@name = "city"]')
    __post_code = (By.XPATH, '//input[@name = "postcode"]')
    __save_address_button = (By.XPATH, '//button[contains(@class , "save")]')

    def set_first_name(self, localization):
        self._send_keys(self.__first_name_input, FakeData.get_name(localization))
        return self

    def set_last_name(self, localization):
        self._send_keys(self.__last_name_input, FakeData.get_last_name(localization))
        return self

    def set_phone_number(self, localization):
        self._send_keys(self.__phone_number_input, FakeData.get_phone_number(localization))
        return self

    def set_address_input(self, localization):
        self._send_keys(self.__address_input, FakeData.get_address(localization))
        return self

    def select_country(self, localization):
        country_code = localization[-2::]
        self._select_element_by_value(self.__country_drop_down, country_code)
        return self

    def select_region(self, localization):
        self._select_element_by_text(self.__region_drop_down, FakeData.get_region(localization))
        return self

    def set_city(self, localization):
        self._send_keys(self.__city_input, FakeData.get_city(localization))
        return self

    def set_post_code(self, localization):
        self._send_keys(self.__post_code, FakeData.get_post_code(localization))
        return self

    def click_save_button(self):
        self._click(self.__save_address_button)

    # def set_name(self, name):
    #     self._send_keys(self.__name_input, name)
    #     return self
    #
    # def set_last_name(self, last_name):
    #     self._send_keys(self.__last_name, last_name)
    #     return self
    #
    # def set_phone_number(self, phone_number):
    #     self._send_keys(self.__phone_number_input, phone_number)
    #     return self
    #
    # def set_address_input(self, address_input):
    #     self._send_keys(self.__address_input, address_input)
    #     return self
    #
    # def select_country(self, country):
    #     self._send_keys(self.__country_drop_down, country)
    #     return self
    #
    # def select_region(self, region):
    #     self._send_keys(self.__region_drop_down, region)
    #     return self
    #
    # def set_city(self, city):
    #     self._send_keys(self.__city_input, city)
    #     return self
    #
    # def set_post_code(self, post_code):
    #     self._send_keys(self.__post_code, post_code)
    #     return self
    #
    # def click_save_button(self):
    #     self._click(self.__save_address_button)
    #

    # def set_name(self, localization):
    #     self._send_keys(self.__name_input, FakeData.get_name(localization))
    #     return self
    #
    # def set_last_name(self, localization):
    #     self._send_keys(self.__last_name, FakeData.get_last_name(localization))
    #     return self
    #
    # def set_phone_number(self, localization):
    #     self._send_keys(self.__phone_number_input, FakeData.get_phone_number(localization))
    #     return self
    #
    # def set_address_input(self, localization):
    #     self._send_keys(self.__address_input, FakeData.get_address(localization))
    #     return self
    #
    # def select_country(self, country):
    #     self._send_keys(self.__country_drop_down, country)
    #     return self
    #
    # def select_region(self, region):
    #     self._send_keys(self.__region_drop_down, region)
    #     return self
    #
    # def set_city(self, city,localization):
    #     self._send_keys(self.__city_input, FakeData.get_city(localization))
    #     return self
    #
    # def set_post_code(self, localization):
    #     self._send_keys(self.__post_code, FakeData.get_post_code(localization))
    #     return self
    #
    # def click_save_button(self):
    #     self._click(self.__save_address_button)
