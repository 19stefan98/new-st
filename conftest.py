import pytest
import chromedriver_binary

from tenderplan.config import config
from helper_selen.screenshot import Screenshot
from selenium import webdriver


# Chrome driver
@pytest.fixture()
def chrome(request):
    options = webdriver.ChromeOptions()
    [options.add_argument(x) for x in config.args]
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    screenshot = Screenshot(driver).screen()
    driver.quit()

# Firefox driver
@pytest.fixture()
def firefox(request):
    options = webdriver.FirefoxOptions()
    [options.add_argument(x) for x in config.args]
    driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver", options=options)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    screenshot = Screenshot(driver).screen()
    driver.quit()
