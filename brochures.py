from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import os
import time
import shutil
import smtplib
from email.message import EmailMessage

# period
today = datetime.date.today()

last_monday = today - datetime.timedelta(days=today.weekday()+7)
monday = datetime.date.strftime(last_monday,"%d/%m/%Y")

last_sunday = today - datetime.timedelta(days=today.weekday()+1)
sunday = datetime.date.strftime(last_sunday,"%d/%m/%Y")

#webscrape and download

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("") #insert Crm url

firstname = driver.find_element_by_name("LogOn1$UserName")
firstname.send_keys("") #username

password = driver.find_element_by_name("LogOn1$Password")
password.send_keys("") #password

password.send_keys(Keys.RETURN)

driver.get("")#correct crm page once logged in

from_date_input = driver.find_elements_by_id("ctl00_ContentPlaceHolder1_ctlStartDate_txtDate")
from_date_input[0].send_keys(monday)

to_date_input = driver.find_elements_by_id("ctl00_ContentPlaceHolder1_ctlEndDate_txtDate")
to_date_input[0].send_keys(sunday)

brochurebutton = driver.find_elements_by_id("ctl00_ContentPlaceHolder1_rboEnquiryTypeBrochure")
brochurebutton[0].click()

submitbutton = driver.find_elements_by_id("ctl00_ContentPlaceHolder1_butGenerate")
submitbutton[0].click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_butAll')))
element.click()

#fileupdate
time.sleep(10) #sleep so file has a chance to download

todayUK = datetime.date.strftime(today,"%d-%m-%Y")
directory = r'' #directory for downloads
recentfile = max([os.path.join(directory,d) for d in os.listdir(directory)], key=os.path.getmtime)

shutil.move(recentfile, r'THE FILE PATH\Brochure Request {}.xls'.format(todayUK))

time.sleep(3)
#send file via email
fromaddr = "" #emails from addr
toaddr = "" # emails to send to

#msg details
msg = EmailMessage()
msg['Subject'] = 'Brochure Requests{}'.format(monday,sunday)
msg['From'] = fromaddr
msg['To'] = toaddr
msg.set_content('AUTOMATED EMAIL & MESSAGE: Please find attached latest brochure requests for the period {} - {}. A copy is also saved in teams>marketing>2021>Brochure Requests. Any issues please contact Charlie.'.format(monday,sunday))

#attaching the file
with open(fileroute,'rb') as f:
    file_data = f.read()
msg.add_attachment(file_data, maintype="application", subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename="Brochure Request {}.xls".format(todayUK))

#accessing server and sending email
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login(fromaddr,'') #username and password for gmail (app pass)
    smtp.send_message(msg)
    smtp.quit()
