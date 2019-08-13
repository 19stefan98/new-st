import pytest
import chromedriver_binary

from tenderplan.config import config
from helper_selen.screenshot import Screenshot
from selenium import webdriver


# Хром драйвер
@pytest.fixture()
def chrome_driver(request):
    options = webdriver.ChromeOptions()
    [options.add_argument(x) for x in config.args]
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    screenshot = Screenshot(driver).screen()
    driver.quit()
