import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demo.openemr.io/b/openemr")
driver.find_element(By.ID,"authUser").send_keys("admin")
driver.find_element(By.ID, "clearPass").send_keys("pass")

select_lan=Select(driver.find_element(By.XPATH,"//select[@name='languageChoice']"))
select_lan.select_by_visible_text("English (Indian)")

driver.find_element(By.ID, "login-button").click()
print(driver.title)
time.sleep(5)

driver.find_element(By.XPATH, "//div[text()='Patient']").click()
driver.find_element(By.XPATH, "//div[text()='New/Search']").click()

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='pat']"))
driver.find_element(By.ID,"form_fname").send_keys("jaswanth")
driver.find_element(By.ID,"form_mname").send_keys("kothabali")
driver.find_element(By.ID,"form_lname").send_keys("reddi gari")
driver.find_element(By.ID,"form_suffix").send_keys("jaswanth reddi gari")
driver.find_element(By.ID,"form_DOB").send_keys("16-07-2000")
driver.find_element(By.ID,"form_sex").send_keys("Male")
driver.find_element(By.ID, "create").click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()











