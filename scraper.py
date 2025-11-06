import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from fake_useragent import UserAgent

def scrape_profiles(profile_urls, progress_callback=None):
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={UserAgent().random}")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.linkedin.com/login')
    time.sleep(2)
    
    # 🔑 Replace these credentials
    driver.find_element(By.ID, 'username').send_keys("sambitsaha201@gmail.com")
    driver.find_element(By.ID, 'password').send_keys("Pass+Word")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)

    profile_data = []
    wait = WebDriverWait(driver, 15)

    for i, url in enumerate(profile_urls, start=1):
        driver.get(url)
        try:
            name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))).text.strip()
        except:
            name = "N/A"
        try:
            headline = driver.find_element(By.XPATH, '//div[contains(@class, "text-body-medium")]').text.strip()
        except:
            headline = "N/A"

        profile_data.append({"Profile URL": url, "Name": name, "Headline": headline})

        if progress_callback:
            progress_callback(i, len(profile_urls))

    driver.quit()
    filename = f"linkedin_profiles_{int(time.time())}.csv"
    df = pd.DataFrame(profile_data)
    df.to_csv(filename, index=False)
    return filename
