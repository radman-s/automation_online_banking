from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator
from .base_page import BasePage

class OnlineBankingPage(BasePage):

    url = 'http://obanksimulator.ngpf.org/'

    @property
    def home(self):
        locator = Locator(By.CSS_SELECTOR, 'a[href="dashboard.php"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def create_acc(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="reg"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="submit_login"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def username(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="member_username"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def password(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="member_password"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def first_name(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="member_first_name"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def question_1(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="select2-member_security_question_id1-container"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def select_1(self):
        locator = Locator(By.XPATH, '//span[text()="What was your childhood nickname?"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def question_2(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="select2-member_security_question_id1-container"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def answer_1(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="member_security_question_answer1"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def answer_2(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="member_security_question_answer2"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def submit(self):
        locator = Locator(By.CSS_SELECTOR, 'button[name="submit"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def deposit_check(self):
        locator = Locator(By.XPATH, '//div[text()="deposit Check"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def choose_acc(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="select2-check_deposit_account_form-container"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def choose_acc_label(self):
        locator = Locator(By.XPATH, '//label[text()="Choose an Account"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def checking_acc(self):
        locator = Locator(By.XPATH, '//span[@aria-activedescendant="select2-check_deposit_account_form-result-gvth-Checking"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def enter_amount(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="check_deposit_amount"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def upload_front(self):
        locator = Locator(By.XPATH, '(//button[@class="upload_btn"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def upload_back(self):
        locator = Locator(By.XPATH, '(//button[@class="upload_btn"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def close_front(self):
        locator = Locator(By.XPATH, '(//button[@class="close"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def close_back(self):
        locator = Locator(By.XPATH, '(//button[@class="close"])[4]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def submit_check(self):
        locator = Locator(By.CSS_SELECTOR, 'button[name="submit"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def success_msg_check(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="alert alert-success alert-dismissable"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def close_alert(self):
        locator = Locator(By.CSS_SELECTOR, 'button[data-dismiss="alert"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def month_date(self):
        locator = Locator(By.XPATH, '(//span[@class="select2-selection__arrow"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def day_date(self):
        locator = Locator(By.XPATH, '(//span[@class="select2-selection__arrow"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def date_go(self):
        locator = Locator(By.CSS_SELECTOR, 'input[value="Go"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def acc_activity(self):
        locator = Locator(By.CSS_SELECTOR, 'a[href="account-activity.php"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def acc_activity_menu(self):
        locator = Locator(By.XPATH, '(//a[text()="account activity"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def acc_activity_sub(self):
        locator = Locator(By.XPATH, '(//a[text()="account activity"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def reset_open(self):
        locator = Locator(By.XPATH, '(//span[@data-toggle="dropdown"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def reset(self):
        locator = Locator(By.XPATH, '(//a[@href="reset_account.php"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def make_transfer(self):
        locator = Locator(By.XPATH, '//div[text()="Make a transfer"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def from_transfer(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="select2-transfer_account_from-container"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def to_transfer(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="select2-transfer_account_to-container"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def amount_transfer(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="transfer_amount"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def submit_transfer(self):
        locator = Locator(By.CSS_SELECTOR, 'button[name="transfer_submit"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def alert(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="alert alert-success alert-dismissable"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def savings_radio(self):
        locator = Locator(By.CSS_SELECTOR, 'label[for="account_type_savings"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def search_acc(self):
        locator = Locator(By.CSS_SELECTOR, 'input[type="search"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def pay_bill(self):
        locator = Locator(By.XPATH, '//div[text()="pay a bill"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def pay_bill_menu(self):
        locator = Locator(By.XPATH, '(//a[text()="pay a bill"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def recipient(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="select2-addPayee-container"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def bill_date(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="bill_pay_date"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def bill_day_third(self):
        locator = Locator(By.XPATH, '(//a[@class="ui-state-default"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def bill_amount(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="bill_pay_amount"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def bill_memo(self):
        locator = Locator(By.CSS_SELECTOR, 'textarea[name="bill_pay_memo"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def bill_submit(self):
        locator = Locator(By.CSS_SELECTOR, 'button[name="submit"]')
        return BaseElement(driver=self.driver, locator=locator)












