from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests

discord_webhook_url = "https://discord.com/api/webhooks/..."

# Open the Browser
driver = webdriver.Chrome()

# Open the Login Page
login_url = "https://elearning.msf-usa.org/mod/scorm/player.php?a=29&currentorg=org_msf_epackage_1&scoid=284&sesskey=Jg6REqPKxL&display=popup&mode=normal"
driver.get(login_url)

# Find Web Elements
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

# Enter Credentials and Submit
username_field.send_keys("YOUR_USERNAME")
password_field.send_keys("YOUR_PASSWORD")
password_field.send_keys(Keys.RETURN)  # Submit the form

# Wait for a moment to let the page load
time.sleep(5)

# Keep track of the elapsed time
start_time = time.time()
stalled = False

driver.switch_to.frame("scorm_object")

while True:
    next_button = driver.find_element(By.CLASS_NAME, "glyphicon-step-forward")
    
    # Check if the button is disabled
    if not next_button.get_attribute("disabled"):

        next_button.click()

        # Reset start_time
        start_time = time.time()

        time.sleep(1)

    else:
        #Stall for user input if the course halts
        if time.time() - start_time > 120 and not stalled:

            discord_message = "ATTENTION REQUIRED: MSF E-Course has stopped progressing. Please check the browser window."
            payload = {
                "content": discord_message
            }
            requests.post(discord_webhook_url, json=payload)
            
            stalled = True # Wait for user input
        
        #timeout after 15 minutes
        if time.time() - start_time > 60*15:
            msg = "Time exceeded 15 minutes. Exiting..."
            payload = {
                "content": msg
            }
            requests.post(discord_webhook_url, json=payload)
            break

# Close the Browser
driver.quit()
