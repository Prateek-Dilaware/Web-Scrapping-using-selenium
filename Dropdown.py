from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome() 
link = "https://the-internet.herokuapp.com/dropdown"
driver.get(link)

dropdown_element = driver.find_element(By.ID,value="dropdown")
s = Select(dropdown_element)

# #select by text
# s.select_by_visible_text("Option 2")

# #select by index
# s.select_by_index(3) #for option -2 

# #select by value
# s.select_by_value("2")


# #counting the options
# count = len(s.options)
# expected =5
# if count == expected:
#     print("All the options are present")
# else:
#     print("All the options are not present") 


target_value = "Option 2"
for o in s.options:
    if o.text == target_value:
        o.click()
        print(f"{target_value} is selected")
        break
    else :
        print(f"Option {target_value} not found") 
        
        
time.sleep(3)
driver.close()

