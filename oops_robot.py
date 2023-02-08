from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Open_emr():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://demo.openemr.io/b/openemr")
    def Open_emrlogin(self):
        self.driver.find_element(By.ID, "authUser").send_keys("admin")
        self.driver.find_element(By.ID, "clearPass").send_keys("pass")
        select_lan = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_lan.select_by_visible_text("English (Indian)")
        self.driver.find_element(By.ID, "login-button").click()

def  Open_emrlogin():
    return 0

class Add_Patient(Open_emr):
    def Patient_details(self):
        self.driver.find_element(By.XPATH, "//div[@class='menuLabel px-1 dropdown-toggle oe-dropdown-toggle']").click()
        self.driver.find_element(By.XPATH, "//div[text()='New/Search']").click()
        self.driver.switch_to.frame("pat")
        self.driver.find_element(By.ID, "form_fname").send_keys("jaswanth")
        self.driver.find_element(By.ID, "form_mname").send_keys("kothabali")
        self.driver.find_element(By.ID, "form_lname").send_keys("reddi gari")
        self.driver.find_element(By.ID, "form_suffix").send_keys("jaswanth reddi gari")
        self.driver.find_element(By.NAME, "form_DOB").send_keys("16-07-2000")
        select_Gender = Select(self.driver.find_element(By.NAME, 'form_sex'))
        select_Gender.select_by_visible_text('Male')
        self.driver.find_element(By.ID, "create").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("modalframe")
        self.driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()

    def validation(self):
        try:
            self.driver.find_element(By.ID, "authUser").click()
        except:
            print("You have entered Invalid id")

obj = Add_Patient()
while True:
    print("Enter 1 login")
    print("Enter 2 after login")
    print("Enter 3 for exception")
    print("Enter 4 for exit code")
    userchoice = int(input("Enter your choice : "))
    if userchoice == 1:
        obj.Open_emrlogin()
    elif userchoice == 2:
        obj.Patient_details()
    elif userchoice == 3:
        obj.validation()
    elif userchoice == 4:
        quit()
