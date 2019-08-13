import pytest
import allure

from tenderplan.constructor.Authorization import Authorization
from tenderplan.constructor.Registration import Registration


@pytest.mark.usefixtures('chrome_driver')
class TestCollector:
    @allure.feature('Регистрация на главной странице')
    def test_registration(self):
        reg = Registration(self.driver).registration()

    @allure.feature('Авторизация')
    def test_authorization(self):
        auth = Authorization(self.driver).authorization()
