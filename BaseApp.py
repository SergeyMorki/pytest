from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://defirex.org/"

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def new_window(self, url):
        current_window = self.driver.current_window_handle
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print(self.driver.current_url)
        try:
            assert self.driver.current_url == url
        except:
            print('Не совпадают url')
        self.driver.close()
        self.driver.switch_to.window(current_window)
