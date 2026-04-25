# test.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil
import sys

# Try to find chromedriver automatically
chromedriver_path = shutil.which("chromedriver")
if not chromedriver_path:
    print("ERROR: chromedriver not found in PATH")
    sys.exit(1)

# Configure Chrome options
options = Options()
options.add_argument("--headless")  # headless mode
options.add_argument("--no-sandbox")  # required for some Linux environments
options.add_argument("--disable-dev-shm-usage")  # overcome limited /dev/shm
options.add_argument("--disable-gpu")  # stable headless execution
options.add_argument("--window-size=1920,1080")  # optional but recommended

# Setup Chrome driver service
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navigate to local site
    driver.get("http://localhost")

    # Wait up to 10 seconds for body tag to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Check page content
    page_content = driver.page_source
    if "Hello CI/CD World" in page_content:
        print("TEST PASSED ✅")
    else:
        print("TEST FAILED ❌")
        sys.exit(1)

finally:
    driver.quit()
