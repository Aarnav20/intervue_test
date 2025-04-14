# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configure Chrome options (optional: headless mode for faster execution without GUI)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open Chrome maximized

# Initialize WebDriver with ChromeDriverManager (auto-manages Chromedriver versions)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Step 1: Open the website
    driver.get("https://www.intervue.io")
    print("Website opened successfully!")
    driver.implicitly_wait(5)

    # Step 2: Click the "Login" button on the top right
    login_button_top_right = driver.find_element(By.LINK_TEXT, "Login")
    login_button_top_right.click()
    print("Clicked the login button on the top right!")
    driver.implicitly_wait(5)

    # Step 3: Click the "Login" button in the middle of the page
    login_button_middle = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")  # Adjust locator if necessary
    login_button_middle.click()
    print("Clicked the login button in the middle of the page!")
    driver.implicitly_wait(5)

    # Step 4: Enter credentials on the login page
    email_field = driver.find_element(By.ID, "email")  # Adjust ID if necessary
    email_field.send_keys("neha@intervue.io")
    
    password_field = driver.find_element(By.ID, "password")  # Adjust ID if necessary
    password_field.send_keys("Ps@neha@123")

    login_submit_button = driver.find_element(By.ID, "login-submit")  # Adjust ID if necessary
    login_submit_button.click()
    print("Submitted login credentials!")
    driver.implicitly_wait(5)

    # Step 5: Type "hello" in the search bar (if available)
    try:
        search_bar = driver.find_element(By.ID, "search-bar")  # Adjust ID if necessary
        search_bar.send_keys("hello")
        print("Typed 'hello' in the search bar!")
        time.sleep(2)  # Optional wait to observe behavior
    except Exception as e:
        print(f"Search bar not found: {e}")
        driver.save_screenshot("search_bar_failure.png")

    # Step 6: Logout by clicking on profile icon and then logout button
    try:
        profile_icon = driver.find_element(By.XPATH, "//div[@class='profile-icon']")  # Adjust locator if necessary
        profile_icon.click()
        logout_button = driver.find_element(By.LINK_TEXT, "Logout")
        logout_button.click()
        print("Logged out successfully!")
    except Exception as e:
        print(f"Logout failed: {e}")
        driver.save_screenshot("logout_failure.png")

except Exception as e:
    print(f"An error occurred: {e}")
    
    # Take a screenshot for any general failure
    driver.save_screenshot("general_failure.png")

finally:
    # Close the browser
    driver.quit()
