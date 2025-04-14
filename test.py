# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options (optional: headless mode for faster execution without GUI)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open Chrome maximized

# Initialize WebDriver with ChromeDriverManager (auto-manages Chromedriver versions)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Step 1: Open the website
    driver.get("https://www.intervue.io")
    print("Website opened successfully!")
    
    # Step 2: Click the "Login" button on the top right
    try:
        top_right_login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        top_right_login_button.click()
        print("Clicked the login button on the top right!")
    except Exception as e:
        print(f"Error locating top-right login button: {e}")
        driver.save_screenshot("top_right_login_failure.png")

    # Step 3: Click the green "Login" button under "For Companies"
    try:
        button = driver.find_element(By.CSS_SELECTOR, '.AccessAccount-ColoredButton-Text[style*="background-color: #008d00"]')
        button.click()
    except Exception as e:
        print(f"Error locating green login button: {e}")
        driver.save_screenshot("green_login_failure.png")

    # Step 4: Enter credentials on the login page (before clicking "Login with email")
    try:
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_email"))
        )
        email_field.send_keys("neha@intervue.io")

        password_field = driver.find_element(By.ID, "login_password")
        password_field.send_keys("Ps@neha@123")

        login_with_email_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'LoginDarkButton-sc-1ertvag-0')]"))
        )
        login_with_email_button.click()
        print("Clicked 'Login with email' button!")
    except Exception as e:
        print(f"Error during login process: {e}")
        driver.save_screenshot("login_failure.png")

    # Step 5: Locate and type into the search bar (based on placeholder span)
    try:
        search_bar_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Search by candidate name, profile etc.']/ancestor::div"))
        )
        search_input = search_bar_container.find_element(By.TAG_NAME, "input")
        search_input.send_keys("hello")
        print("Typed 'hello' in the search bar!")
    except Exception as e:
        print(f"Search bar not found or interaction failed: {e}")
        driver.save_screenshot("search_bar_failure.png")

    # Step 6: Click on profile dropdown (using inspect element provided)
    try:
        profile_dropdown_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//i[@class='anticon' and @style='margin-left: 7px; font-size: 10px; transform: rotate(0deg); transition: 300ms;']"))
        )
        profile_dropdown_icon.click()
        print("Profile dropdown clicked!")
    except Exception as e:
        print(f"Profile dropdown not found or interaction failed: {e}")
        driver.save_screenshot("profile_dropdown_failure.png")

    # Step 7: Click Logout button (using inspect element provided)
    try:
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='Dropdown__DropdownItemLink-k60emx-2 hHnuKn' and @href='/logout']"))
        )
        logout_button.click()
        print("Logout clicked!")
    except Exception as e:
        print(f"Logout button not found or interaction failed: {e}")
        driver.save_screenshot("logout_failure.png")

except Exception as e:
    print(f"An error occurred during execution: {e}")
    
    # Take a screenshot for any general failure
    driver.save_screenshot("general_failure.png")

finally:
    # Close the browser
    driver.quit()
