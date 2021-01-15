from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

# from_date = input("Please enter FROM date in DD/MM/YYYY format ONLY: ")
# to_date = input("Please enter TO date in DD/MM/YYYY format ONLY: ")

today = datetime.date.today()

last_monday = today - datetime.timedelta(days=today.weekday()+7)
monday = datetime.date.strftime(last_monday,"%d/%m/%Y")

last_sunday = today - datetime.timedelta(days=today.weekday()+1)
sunday = datetime.date.strftime(last_sunday,"%d/%m/%Y")


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("INITAL WEBSITE TO OPEN")

firstname = driver.find_element_by_name("LogOn1$UserName")
firstname.send_keys("ENTER USERNAME")

password = driver.find_element_by_name("LogOn1$Password")
password.send_keys("ENTER PASSWORD")

password.send_keys(Keys.RETURN)

driver.get("NAVIGATE TO NEW PAGE")

#getting the previous monday -7days

from_date_input = driver.find_elements_by_id("ID")
from_date_input[0].send_keys(monday)

#previous sunday 

to_date_input = driver.find_elements_by_id("ID")
to_date_input[0].send_keys(sunday)

brochurebutton = driver.find_elements_by_id("ID")
brochurebutton[0].click()

submitbutton = driver.find_elements_by_id("ID")
submitbutton[0].click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'ID')))
element.click()

