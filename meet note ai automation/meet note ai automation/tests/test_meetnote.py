import pytest
from drivers.browser_setup import init_driver
from pages.login_page import LoginPage
from pages.meeting_page import MeetingPage

@pytest.fixture
def driver():
    driver = init_driver()
    yield driver
    driver.quit()

def test_add_meeting(driver):
    login_page = LoginPage(driver)
    meeting_page = MeetingPage(driver)

    login_page.open()
    login_page.login("sandeepraj34@yopmail.com", "7075835053")
    meeting_page.add_meeting("config/data.properties")