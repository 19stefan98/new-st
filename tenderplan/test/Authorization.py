from tenderplan.page.AuthorizationPage import AuthorizationPage
from tenderplan.page.PersonalCabinet import PersonalCabinet
from tenderplan.data.data import Data


class Authorization(AuthorizationPage):
    def authorization(self):
        self.url()
        self.login(Data.login)
        self.password(Data.password)
        self.button_login_in()
        self.result = PersonalCabinet(self.driver)
        assert "тендерплан" in self.result.result_auth()
