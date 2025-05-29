from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://meetnote.ai")



    def login(self, email, password):
        login_button_xpath = "//button[normalize-space()='Login']"
        email_field_id = "email-address"
        password_field_id = "password"
        submit_button_xpath = "//button[@type='submit']"

        # Wait for and click the login button using ActionChains
        self.wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
        login_button = self.driver.find_element(By.XPATH, login_button_xpath)

        # Ensure element is in view (just in case)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'instant', block: 'center' });",
                                   login_button)

        # Perform the click using ActionChains
        ActionChains(self.driver).move_to_element(login_button).click().perform()

        def is_logged_in(self):
            try:
                return self.driver.find_element(*self.dashboard_element).is_displayed()
            except:
                return False


        # Wait for email field to appear and enter credentials
        self.wait.until(EC.visibility_of_element_located((By.ID, email_field_id))).send_keys(email)
        self.driver.find_element(By.ID, password_field_id).send_keys(password)

        # Submit the form
        self.wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath))).click()
