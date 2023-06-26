from selenium.webdriver.common.by import By
from pageObjects.baseElement import Elements as ele

class AboutYouNegativeProcess:

    def __init__(self,driver):
        self.driver=driver

    def setFirstName(self, firstName):
        fname = self.driver.find_element(By.NAME, ele.first_name)
        if fname.is_displayed() and fname.is_enabled():
            fname.clear()
            fname.send_keys(firstName)
            # self.driver.save_screenshot(".\\screenshots\\"+"FirstNameValid.png")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"FirstNameFieldError.png")

    def setLastName(self, lastName):
        lname = self.driver.find_element(By.NAME, ele.last_name)
        if lname.is_displayed() and lname.is_enabled():
            lname.clear()
            lname.send_keys(lastName)
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"LastNameFieldError.png")

    def setUniversityEmail(self, universityEmail):
        u_email = self.driver.find_element(By.NAME, ele.university_email)
        if u_email.is_displayed() and u_email.is_enabled():
            u_email.clear()
            u_email.send_keys(universityEmail)
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "UniversityEmailFieldError.png")

    def setPersonalEmail(self, personalEmail):
        email = self.driver.find_element(By.NAME, ele.personal_email)
        if email.is_displayed() and email.is_enabled():
            email.clear()
            email.send_keys(personalEmail)
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "PersonalEmailFieldError.png")

    def setMobileNumber(self, mobileNumber):
        number = self.driver.find_element(By.NAME, ele.mobile_number)
        if number.is_displayed() and number.is_enabled():
            number.clear()
            number.send_keys(mobileNumber)
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "MobileNumberFieldError.png")

    def setDateOfBirth(self, dateOfBirth):
        dob = self.driver.find_element(By.NAME, ele.date_of_birth)
        if dob.is_displayed() and dob.is_enabled():
            dob.clear()
            dob.send_keys(dateOfBirth)
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "DateOfBirthFieldError.png")

    def setGender(self, gender):
        g = self.driver.find_element(By.XPATH, "//input[@id ='" + gender + "']")
        if g.is_displayed():
            # g.clear()
            g.click()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "GenderFieldError.png")

    def clickGotoSecondPage(self):
        self.driver.find_element(By.ID, self.button_page_one).click()