from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser

class MeetingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_meeting(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        if not config.has_section('details'):
            raise Exception("Missing [details] section in config file.")

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Add to Meeting']"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Subject for the Meeting']"))).send_keys(config.get('details', 'meeting_subject'))
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Meeting Link']").send_keys(config.get('details', 'meeting_link'))
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()