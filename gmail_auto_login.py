from selenium import webdriver
from browserdriver import browser_config

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(browser_config.get_driver_path())
driver.get("http://www.gmail.com")

loginId = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='identifierId']")))
loginId.send_keys("xxxx@gmail.com")

WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "identifierNext"))).click()

password = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//*[@name='password']")))
password.send_keys("xxxxx")

WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "passwordNext"))).click()

numbers = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,"//*[@class='J-J5-Ji amH J-JN-I']")))
start = 0
end = 0
maxNum = 0
if numbers:
    numStr = numbers.text
    arr = numStr.split(' ')
    startNumStr = arr[0]
    startArr = startNumStr.split('–')
    start = int(startArr[0])
    end = int(startArr[1])
    maxNum = int(arr[2].replace(',', ""))
    print(str(start) + " " + str(end) + " " + str(maxNum))

total_loop = maxNum / end

count = 0

import pdb; pdb.set_trace()
while count != total_loop:
    try:
        select_all = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//*[@class='T-Jo J-J5-Ji']")))
        select_all.click()
    except Exception:
        print("Exception while selecting all mails for count: " + str(count))

    try:
        mark_as_read = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//*[@class='T-I J-J5-Ji m9 T-I-ax7 L3']")));
        mark_as_read.click()
    except Exception:
        print("Exception mark as read")

    try:
        next_page = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//*[@class='T-I J-J5-Ji amD T-I-awG T-I-ax7 T-I-Js-Gs L3']")))
        next_page.click()
    except Exception:
        print("Exception for getting next page for count: " + str(count))

    count = count + 1

driver.close()










