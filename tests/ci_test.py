import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_submit_form(driver):
    file_path = "file://" + os.path.abspath("index.html")

    driver.get(file_path)

    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "age").send_keys("25")
    driver.find_element(By.ID, "date").send_keys("2025-01-01")

    driver.find_element(By.ID, "submit").click()

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert message.text == "Form submitted successfully"
