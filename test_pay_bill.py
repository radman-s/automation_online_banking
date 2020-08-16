from pages.drivers import Drivers
from pages.online_banking_page import OnlineBankingPage
from pages.base_tree import Root
from pages.accounts_acttivity_table import Listings

browser = Drivers('--start-maximized').chrome()
obp = OnlineBankingPage(driver=browser)

# test setup
user = 'Bruce Lee'
pw = 'password'
check_mark = '✔'
amount = '150.0'
clearence_date = '2017-01-04'

# test start
# login
obp.go()
obp.username.input_text(user)
obp.password.input_text(pw)
obp.login.click()

# reset acc
obp.reset_open.click()
obp.reset.click()

# pay a bill
obp.pay_bill.click()
obp.recipient.click()
obp.recipient.arrow_down()
obp.recipient.enter()

# get recipient name for later validation
rec_name = obp.recipient.text()

obp.bill_date.click()
obp.bill_day_third.click()
obp.bill_amount.input_text(amount)
obp.bill_memo.input_text('Thank you for everything')
obp.bill_submit.click()
alr = obp.alert.text()
print(alr)
print()

# forward date by 4 days
obp.day_date.click()

# arrow down three times
count = 0
while count < 3:
    obp.day_date.arrow_down()
    count += 1
else:
    obp.day_date.enter()
obp.date_go.click()

# switch to account activity
obp.home.click()
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
name = checking_firs_row.name

# assert correct recipient name
assert name.lower() == rec_name.lower()
print(f'expected recipient name:          {rec_name}')
print(f'recipient name:                   {name}', check_mark)

# assert the correct amount left the checking acc
assert float(amount) == checking_amount_sent

print(f'checking balance before bill:     {checking_balance_before}')
print(f'transfer amount sent:             {checking_amount_sent}')
print(f'checking balance after bill:      {checking_balance_after}', check_mark)
difference_checking = round(checking_balance_before - checking_balance_after)
assert difference_checking == checking_amount_sent
print('checking account ok')
print()

# forward date by one month
obp.month_date.click()
obp.month_date.arrow_down()
obp.month_date.enter()
obp.date_go.click()

# lxml setup get new listings
html = browser.page_source
listing = Root(html, locator='.//tbody/tr')
checking_firs_row = listing.get_listings(Listings)[0]

checking_amount_sent = float(checking_firs_row.amount[2:])

# assert correct recipient name
print('one month later')
print()
name = checking_firs_row.name
assert name.lower() == rec_name.lower()
print(f'expected recipient name:          {rec_name}')
print(f'recipient name:                   {name}', check_mark)

# assert the correct amount left the checking acc
assert float(amount) == checking_amount_sent
print(f'transfer amount sent:             {checking_amount_sent}')
print()
browser.quit()
print('Test passed.')
