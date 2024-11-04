from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
user = "standard_user"
passs = "secret_sauce"
login_url = driver.get("https://www.saucedemo.com/v1/")

username_field = driver.find_element(By.ID,value="user-name")
password_field = driver.find_element(By.ID,value="password" )

#filling the values
username_field.send_keys(user)
password_field.send_keys(passs)

#locator
login_button = driver.find_element(By.ID,value="login-button")
assert not login_button.get_attribute("disabled")
login_button.click()

sucess_element = driver.find_element(By.CSS_SELECTOR,value=".product_label")
assert sucess_element.text == 'Products'

print("sucess")
