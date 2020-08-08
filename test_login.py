from selenium import webdriver
from pages.online_banking_page import OnlineBankingPage
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)

obp = OnlineBankingPage(driver=browser)

# test setup
user = 'Bruce Lee'
pw = 'password'
name = 'George'
sa1 = 'answer1'
sa2 = 'answer2'

obp.go()
obp.username.input_text(user)
obp.password.input_text(pw)
obp.login.click()







