from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Create a new instance of the web driver
driver = webdriver.Firefox

try:
    # Open the website
    driver.get("https://www.saucedemo.com/")

    # Display cookies before login
    print("Cookies before login:")
    for cookie in driver.get_cookies():
        print(cookie)

    # Find the username and password input fields
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")

    # Enter the credentials
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for a few seconds to ensure the page loads
    time.sleep(3)

    # Display cookies after login
    print("\nCookies after login:")
    for cookie in driver.get_cookies():
        print(cookie)

    # Perform logout
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()

    time.sleep(1)  # Wait for the menu to open

    logout_link = driver.find_element(By.ID, "logout_sidebar_link")
    logout_link.click()

    # Wait for a few seconds to ensure logout
    time.sleep(3)

    # Display cookies after logout
    print("\nCookies after logout:")
    for cookie in driver.get_cookies():
        print(cookie)

finally:
    # Close the browser
    driver.quit()
