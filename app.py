import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pywhatkit
from datetime import datetime
 

driver = webdriver.Chrome('./chromedriver')
url = "https://visa.vfsglobal.com/tur/en/pol/login"
email = ""
password = ""
counter = 0

def login(url, email, password):
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/app-root/div/app-login/section/div/div/mat-card/form/div[1]/mat-form-field/div/div[1]/div[3]/input").send_keys(email)
    driver.find_element_by_xpath("/html/body/app-root/div/app-login/section/div/div/mat-card/form/div[2]/mat-form-field/div/div[1]/div[3]/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/app-root/div/app-login/section/div/div/mat-card/form/button/span[1]").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/app-root/div/app-dashboard/section/div/div[1]/div[2]/button/span[1]").click()
    time.sleep(3)
    control()


def control():
    global counter
    #Country
    driver.find_element_by_xpath("/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[1]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[1]/span").click()
    time.sleep(4)

    if counter%2 == 0:
        #Ankara
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/mat-option[1]/span").click()
    else:
        #Antalya
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/mat-option[1]/span").click()
    time.sleep(4)
    #Visa Type
    driver.find_element_by_xpath("/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[2]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[1]/span").click()
    time.sleep(4)
    #Type D
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/mat-option[1]/span").click() 
    time.sleep(4)
    #Sub Category
    driver.find_element_by_xpath("/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[3]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[1]/span").click()
    time.sleep(4)
    #Education
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/mat-option[1]/span").click()
    time.sleep(4)

    result = driver.find_element_by_xpath("/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[4]/div").text
    counter += 1
    if "Available Slot" in result:
        sendMessage(result)
    else:
        if counter%2 == 0:
            time.sleep(300)
        control()

def sendMessage(result):
    global counter
    now = datetime.now()
    hour = int(now.strftime("%H"))
    minute = int(now.strftime("%M"))
    if minute == 59:
        minute += 2
        hour += 1
    else:
        minute += 1
    
    if counter%2 == 1:
        result = result + " Ankara"
    else:
        result = result + " Antalya"

    pywhatkit.sendwhatmsg("+9*******",
                      result ,
                      int(hour), int(minute))
login(url,email,password)
