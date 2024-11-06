from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
link = "https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"

driver.get(link)
driver.maximize_window()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

try :
    checkboxes = driver.find_elements(By.XPATH,value="//input[@type='checkbox']")
    for check in checkboxes:
        if not check.is_selected():
            check.send_keys(Keys.SPACE)
        print("Checkboxes filled successfully")
except Exception as e:
    print(f'An error occured:- {e}')
    
    
#counting the checkboxes
print()
print("*********Verifying all the checkboxes as been filled*****")
count = 0 
for check in checkboxes:
    if check.is_selected():
        count +=1
        
expected_counts = 7

if count == expected_counts:
    print("All checkboxes are verified ")
else:
    print("checkBox count mismatch")
    
time.sleep(5)
driver.close()
        