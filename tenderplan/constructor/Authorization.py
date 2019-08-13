from tenderplan.page.AuthorizationPage import AuthorizationPage
from tenderplan.page.PersonalCabinet import PersonalCabinet
from tenderplan.config import config


class Authorization(AuthorizationPage):
    def authorization(self):
        self.url()
        self.login(config.login)
        self.password(config.password)
        self.button_login_in()
        self.result = PersonalCabinet(self.driver)
        assert "тендерплан" in self.result.result_auth()
