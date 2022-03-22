from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(5)

value1 = 15
value2 = 20


try:
    no_thanks_btn = driver.find_element(By.CLASS_NAME, value='at-cm-no-button')
    no_thanks_btn.click()
except:
    print("No element with such name, so we skipp it")

input_field_1 = driver.find_element(By.ID, value='sum1')
input_field_2 = driver.find_element(By.ID, value='sum2')

input_field_1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
input_field_2.send_keys(value2)

# find element by CSS Selector
get_value_btn = driver.find_element(By.CSS_SELECTOR, value='button[onclick="return total()"]')
get_value_btn.click()

