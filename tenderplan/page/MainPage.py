import allure

from tenderplan.data.locators import Locators
from tenderplan.config import config
from tenderplan.base import Base


class MainPage(Base):
    @allure.step('Переходит на главную страницу')
    def url(self):
        self.driver.get(config.url)

    @allure.step('Вводит "Имя и фамилию"')
    def name(self, name):
        return self.wait.find_by_class_name_of_wait(Locators.input_reg).send_keys(name)

    @allure.step('Вводит "Название компании"')
    def company_name(self, company_name):
        company_index = self.wait.find_by_class_name_of_all_wait(Locators.input_reg)
        company = company_index[1]
        return company.send_keys(company_name)

    @allure.step('Вводит "Электронную почту"')
    def email(self, email):
        email_index = self.wait.find_by_class_name_of_all_wait(Locators.input_reg)
        emai_l = email_index[2]
        return emai_l.send_keys(email)

    @allure.step('Вводит "Телефон"')
    def phone(self, email):
        phone_index = self.wait.find_by_class_name_of_all_wait(Locators.input_reg)
        phon_e = phone_index[3]
        return phon_e.send_keys(email)

    @allure.step('Вводит "Пароль"')
    def password(self, password):
        password_index = self.wait.find_by_class_name_of_all_wait(Locators.input_reg)
        passwor_d = password_index[4]
        return passwor_d.send_keys(password)

    @allure.step('Кликает по кнопке "Зарегистрироваться"')
    def button_reg(self):
        self.wait.find_by_class_name_of_wait(Locators.button_reg).click()
