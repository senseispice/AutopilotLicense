from selenium import webdriver
import json
import time

try:
    # Open the Browser
    driver = webdriver.Chrome()

    # Go to page
    target_url = "https://courses.boatus.org/courses/purchased" 
    driver.get(target_url)

    pathname = '.../cookies.json'
    with open(pathname, "r") as file:
        cookies = json.load(file)

    # Filter cookies and add each cookie to the browser session
    for cookie in cookies:
        if not cookie.get("sameSite") or cookie["sameSite"] not in ["Strict", "Lax", "None"]:
            cookie["sameSite"] = "None"
        driver.add_cookie(cookie)
    
    # Refresh the page to apply the cookies
    driver.refresh()
    time.sleep(30)

    # Now you should be able to access the site without login

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()