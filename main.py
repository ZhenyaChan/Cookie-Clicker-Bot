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

# find upgrades/items in the store
store_items = [item for item in driver.find_elements(By.CSS_SELECTOR, value="#rightPanel #store div")]
# for item in store_items:
#     print(item.text)



# driver.quit()
