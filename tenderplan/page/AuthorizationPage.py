import allure

from tenderplan.data.locators import Locators
from tenderplan.data.url import Url
from tenderplan.config import config
from tenderplan.base import Base


class AuthorizationPage(Base):
    @allure.step('Переходит на страницу авторизации')
    def url(self):
        self.driver.get(config.url + Url.url_auth)

    @allure.step('Вводит логин')
    def login(self, param):
        login_index = self.wait.find_by_class_name_of_all_wait(Locators.login)
        login = login_index[0]
        return login.send_keys(param)

    @allure.step('Вводит пароль')
    def password(self, pas):
        pass_index = self.wait.find_by_class_name_of_all_wait(Locators.login)
        password = pass_index[1]
        return password.send_keys(pas)

    @allure.step('Кликает по кнопке Войти')
    def button_login_in(self):
        self.wait.find_by_class_name_of_wait(Locators.login_in).click()
