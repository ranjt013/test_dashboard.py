
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

EMAIL     = "qa@segwise.ai"
PASSWORD  = "segwise_test"
LOGIN_URL = "https://ua.segwise.ai/login"
DASHBOARD = "https://ua.segwise.ai/qa_assignment/home"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

try:
   
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    ).send_keys(EMAIL)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    WebDriverWait(driver, 10).until(EC.url_contains("segwise"))
    if not driver.current_url.startswith(DASHBOARD):
        driver.get(DASHBOARD)
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(., 'Overview')]"))
    )
    print("✅ Overview chart found – smoke test passed.")

finally:
    driver.quit()
