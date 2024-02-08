from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Use Chrome driver (change if different browser)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Find cookie element for clicking
cookie = driver.find_element(By.ID, value="cookie")

# Find upgrades/items in the store
store_items = [item for item in driver.find_elements(By.CSS_SELECTOR, value="#rightPanel #store div") if item.text != ""]
# for item in store_items:
#     print(item.text)

# Find items id
items_ids = [item.get_attribute("id") for item in store_items if item.text != ""]

# Helper Functions:
# Find price of the item function
def get_price(item_value):
    item_price = item_value.find_element(By.TAG_NAME, value="b")
    return int(item_price.text.split("-")[1].replace(",", ""))


# Find all prices of the items
def all_prices():
    store = [int(item.text.split("-")[1].replace(",", "")) for item in
             driver.find_elements(By.CSS_SELECTOR, value="#store b") if item.text != "" ]
    return store


# Get money
def get_money():
    money = int(driver.find_element(By.ID, value="money").text.strip().replace(",", ""))
    return money


# 5 minutes from now
five_mins = time.time() + 60 * 5
# 5 seconds
timeout = time.time() + 5

# Run the bot for 5 minutes
while True:
    cookie.click()

    # Check for upgrades every 5 seconds
    if time.time() > timeout:
        # Get all prices
        items_prices = all_prices()
        # Get current amount of money
        available_money = get_money()

        # Find the available items to buy
        all_items = {}
        for n in range(len(items_prices)):
            if available_money > items_prices[n]:
                all_items[items_prices[n]] = items_ids[n]

        # Find and click the most expensive item from the list
        max_price = max(all_items)
        buy_item_id = all_items[max_price]
        buy_item = driver.find_element(By.ID, value=buy_item_id)
        buy_item.click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After five minutes
    if time.time() > five_mins:
        cookies_per_sec = driver.find_element(By.ID, value="cps")
        print(cookies_per_sec.text)
        break

# driver.quit()
