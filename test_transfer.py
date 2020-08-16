from pages.drivers import Drivers
from pages.online_banking_page import OnlineBankingPage
from pages.accounts_acttivity_table import Listings
from pages.base_tree import Root
import time

browser = Drivers('--start-maximized').chrome()
obp = OnlineBankingPage(driver=browser)

# test setup
user = 'Bruce Lee'
pw = 'password'
check_mark = '✔'

# test start
# login
obp.go()
obp.username.input_text(user)
obp.password.input_text(pw)
obp.login.click()

# reset acc
obp.reset_open.click()
obp.reset.click()

# change date
obp.day_date.click()
obp.day_date.arrow_down()
obp.day_date.enter()
obp.date_go.click()

obp.make_transfer.click()
# from checking acc
obp.from_transfer.click()
obp.from_transfer.arrow_down()
obp.from_transfer.enter()
# to savings acc
obp.to_transfer.click()
obp.to_transfer.arrow_down()
obp.to_transfer.enter()

obp.amount_transfer.input_text('200.0')
obp.submit_transfer.click()
alert = obp.alert.text()
print(f'{alert}')
print(' ')

obp.acc_activity.click()
# lxml setup
html = browser.page_source
listing = Root(html, locator='.//tbody/tr')
checking_firs_row = listing.get_listings(Listings)[0]
checking_second_row = listing.get_listings(Listings)[1]

# remove the currency symbols
checking_amount_sent = float(checking_firs_row.amount[2:])
checking_balance_after = float(checking_firs_row.balance[1:])
checking_balance_before = float(checking_second_row.balance[1:])

# assert the correct amount left the checking acc
print(f'checking balance before transfer: {checking_balance_before}')
print(f'transfer amount sent:             {checking_amount_sent}')
print(f'checking balance after transfer:  {checking_balance_after}', check_mark)
difference_checking = round(checking_balance_before - checking_balance_after)
assert difference_checking == checking_amount_sent
print('checking account ok')
print(' ')

# switch to savings acc
obp.acc_activity_menu.click()
obp.acc_activity_sub.click()
time.sleep(2)
obp.savings_radio.move_to()
obp.savings_radio.click()
time.sleep(2)
browser.refresh()

# refresh listings
html = browser.page_source
listing = Root(html, locator='.//tbody/tr')
savings_firs_row = listing.get_listings(Listings)[0]
savings_second_row = listing.get_listings(Listings)[1]

# assert the correct amount was received to savings acc
savings_amount_received = float(savings_firs_row.amount[1:])
savings_balance_after = float(savings_firs_row.balance[1:])
savings_balance_before = float(savings_second_row.balance[1:])
print(f'savings balance before transfer:  {savings_balance_before}')
print(f'transfer amount received:         {savings_amount_received}')
print(f'savings balance after transfer:   {savings_balance_after}', check_mark)
difference_savings = savings_balance_after - savings_balance_before
assert difference_savings == savings_amount_received
print('savings account ok')
browser.quit()
print('test passed')









