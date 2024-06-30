import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configure options for headless operation
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Path to the latest file
file_path = os.getenv('FILE')
whatsapp_group_name = os.getenv('Testing')

# Set up the Chrome WebDriver
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code
print("Scan the QR code to log in to WhatsApp Web...")
time.sleep(15)  # Adjust this time based on how long it takes to scan QR code

# Search for the WhatsApp group
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
time.sleep(1)
search_box.send_keys(whatsapp_group_name)
search_box.send_keys(Keys.ENTER)
time.sleep(2)

# Upload and send the file
attachment_box = driver.find_element(By.XPATH, '//div[@title="Attach"]')
attachment_box.click()
time.sleep(1)

file_input = driver.find_element(By.XPATH, '//input[@accept="*"]')
file_input.send_keys(os.path.abspath(file_path))
time.sleep(2)

send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
send_button.click()
time.sleep(5)

print("File sent successfully.")
driver.quit()
