import pytest

from aqa_framework.page_object.home_page import HomePage
from aqa_framework.page_object.login_page import LoginPage
from aqa_framework.page_object.product_detais_page import PDP
from aqa_framework.page_object.register_page import RegisterPage
from aqa_framework.utilities.config_parser import ReadConfig
from aqa_framework.utilities.driver_factory import DriverFactory


# @pytest.fixture(scope='session')
# @pytest.fixture()
# @pytest.fixture(scope='session')
@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_browser_id())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    create_driver.get(ReadConfig.get_login_page_url())
    return LoginPage(create_driver)


@pytest.fixture()
def open_register_page(create_driver):
    create_driver.get(ReadConfig.get_register_page_url())
    return RegisterPage(create_driver)


@pytest.fixture()
def login(open_login_page):
    return open_login_page.login(ReadConfig.get_email(), ReadConfig.get_password())


@pytest.fixture(scope='session')
def localization_pl():
    return 'pl_PL'


@pytest.fixture()
def open_cart_page(login):
    dashboard_page = login
    return dashboard_page.click_reorder_button()


@pytest.fixture()
def open_pdp(login, create_driver):
    login
    create_driver.get(ReadConfig.get_base_url())
    HomePage(create_driver).go_to_pdp()
    return PDP(create_driver)


    # home_page = HomePage(create_driver.get(ReadConfig.get_base_url()))
    # pdp = home_page.go_to_pdp()
    # return pdp


