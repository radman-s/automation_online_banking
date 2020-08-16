from pages.drivers import Drivers
from pages.online_banking_page import OnlineBankingPage
from pages.base_tree import Root
from pages.accounts_acttivity_table import Listings

browser = Drivers('--start-maximized').chrome()
obp = OnlineBankingPage(driver=browser)

# test setup
user = 'Bruce Lee'
pw = 'password'
expect_date = '2017-01-05'
check_mark = '✔'
payed_amount = float(5000.0)

# login
obp.go()
obp.username.input_text(user)
obp.password.input_text(pw)
obp.login.click()

# Reset Account
obp.reset_open.click()
obp.reset.click()

# deposit check
obp.deposit_check.click()
obp.choose_acc.click()
obp.choose_acc.arrow_down()
obp.choose_acc.enter()
obp.enter_amount.input_text('5000')
obp.upload_front.click()
obp.close_front.click()
obp.upload_back.click()
obp.close_back.click()
obp.submit.click()
alert = obp.success_msg_check.text()
print(f'Alert appeared:\n{alert}')
obp.close_alert.click()

# simulate date + 4 days for the check to be cleared.
obp.day_date.click()
# press arrow down four times in date drop down menu.
count = 0
while count < 4:
    obp.day_date.arrow_down()
    count += 1
else:
    obp.day_date.enter()
obp.date_go.click()
obp.acc_activity.click()
browser.refresh()

# acc activity scrub with etree
# setup
html = browser.page_source
listing = Root(html, locator='.//tbody/tr')
firs_row = listing.get_listings(Listings)[0]
second_row = listing.get_listings(Listings)[1]
id_1 = firs_row.id
date_1 = firs_row.date

# remove currency sign and decimal separator
amount_1 = float(firs_row.amount[1:].replace(',', ''))
balance_before_pay = float(second_row.balance[1:].replace(',', ''))
balance_after_pay = float(firs_row.balance[1:].replace(',', ''))

# validate the check was cleared in 4 days
assert date_1 == expect_date
print(f'expected date:      {expect_date}')
print(f'clearence date:     {date_1}',check_mark)

# validate correct deposit amount
acc_amount = amount_1
print(f'amount payed:       {payed_amount}')
print(f'amount received:    {acc_amount}', check_mark)
assert acc_amount == payed_amount

# validate deposit amount was added to the current balance
print(f'balance before pay:  {balance_before_pay}')
print(f'balance after pay: {balance_after_pay}', check_mark)
assert balance_after_pay - balance_before_pay == payed_amount

browser.quit()
print('Test passed')










