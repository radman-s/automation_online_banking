from pages.drivers import Drivers
from pages.online_banking_page import OnlineBankingPage

browser = Drivers('--start-maximized').chrome()
obp = OnlineBankingPage(driver=browser)

# test setup
user = 'Bruce Lee'
pw = 'password'
name = 'George'
sa1 = 'answer1'
sa2 = 'answer2'

# test start
obp.go()
obp.username.input_text(user)
obp.password.input_text(pw)
obp.login.click()
print('test passed')







