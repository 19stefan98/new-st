import pytest
import allure

from tenderplan.test.Authorization import Authorization
from tenderplan.test.Registration import Registration
from tenderplan.config import config


@pytest.mark.usefixtures(config.browser)
class TestCollector:
    @allure.feature('Регистрация на главной странице')
    def test_registration(self):
        reg = Registration(self.driver).registration()

    @allure.feature('Авторизация')
    def test_authorization(self):
        auth = Authorization(self.driver).authorization()
