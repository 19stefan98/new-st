from helper_selen.helper import Helper
from helper_selen.screenshot import Screenshot


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = Helper(self.driver)
        self.screen = Screenshot(self.driver)

    def scr(self):
        self.screen.screen()
