from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    def select_dropdown(self, val):
        element = Select(self.web_element)
        element.select_by_value(val)
        return None

    def text(self):
        text = self.web_element.text
        return text

    def move_to(self):
        element = ActionChains(self.driver)
        element.move_to_element(self.web_element).perform()
        return None

    def move_mouse(self, x, y):
        ActionChains(self.driver).move_by_offset(x,y).perform()
        return None

    def arrow_down(self):
        element = ActionChains(self.driver)
        element.send_keys(Keys.ARROW_DOWN).perform()
        return None

    def enter(self):
        element = ActionChains(self.driver)
        element.send_keys(Keys.ENTER).perform()
        return None


