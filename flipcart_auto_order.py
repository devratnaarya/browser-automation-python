
from chromdriver import browser_config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(browser_config.get_driver_path())

driver.get("https://www.flipkart.com/account/login?ret=/")
driver.maximize_window()

# wait for Fastrack menu item to appear, then click it
loginId = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//*[@class='_2zrpKA']")));
loginId.send_keys("adevratna@gmail.com") #_2AkmmA _1LctnI _7UHT_c

password = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//*[@class='_2zrpKA _3v41xv']")));
password.send_keys("dev1994arya")

driver.find_element_by_xpath("//*[@class='_2AkmmA _1LctnI _7UHT_c']").click()



