import time

from tenderplan.page.MainPage import MainPage
from tenderplan.page.PersonalCabinet import PersonalCabinet
from helper_selen.generation import Generation
from tenderplan.data.data import Data


class Registration(MainPage):
    def registration(self):
        rand = Generation(self.driver).random()
        self.url()
        self.name(Data.name)
        self.company_name(Data.company_name)
        self.email(rand + Data.email)
        self.phone(Data.phone)
        self.password(Data.password)
        self.button_reg()
        time.sleep(5)
        self.result = PersonalCabinet(self.driver)
        assert "Добро пожаловать в Тендерплан" in self.result.result_reg()
