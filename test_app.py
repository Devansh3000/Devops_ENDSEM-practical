from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def test_button_click():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = f"file:///{current_dir}/index.html".replace("\\", "/")

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(file_path)

        header = driver.find_element(By.ID, "header")
        assert header.text == "Hello"

        btn = driver.find_element(By.ID, "btn")
        btn.click()

        header = driver.find_element(By.ID, "header")
        assert header.text == "Clicked!", f"Expected 'Clicked!', got '{header.text}'"

        print("Selenium test passed successfully!")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_button_click()
