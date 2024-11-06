from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 


driver.maximize_window()
#driver.minimize_window()
#driver.fullscreen_window()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,value=".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(5)
driver.close()