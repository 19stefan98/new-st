import allure

from tenderplan.data.locators import Locators
from tenderplan.base import Base


class PersonalCabinet(Base):
    @allure.step('Парсит текст c лого')
    def result_auth(self):
        return self.wait.find_by_class_name_of_wait(Locators.result_auth).text

    @allure.step('Парсит текст с поп апа регистрации')
    def result_reg(self):
        return self.wait.find_by_tag_name_of_wait(Locators.res_reg).text
