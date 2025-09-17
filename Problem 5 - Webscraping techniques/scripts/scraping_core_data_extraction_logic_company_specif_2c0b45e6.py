```python
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytesseract
from PIL import Image
import json
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure paths for ChromeDriver and Tesseract
CHROME_DRIVER_PATH = '/path/to/chromedriver'
TESSERACT_CMD = '/path/to/tesseract'
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

# List of company URLs to scrape
company_urls = [
    "https://www.examplecompany1.com",
    "https://www.examplecompany2.com",
    "https://www.examplecompany3.com",
    "https://www.examplecompany4.com",
    "https://www.examplecompany5.com"
]

def fetch_webpage(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        logging.error(f"Timeout occurred while fetching {url}")
        raise TimeoutException
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occurred: {e}")
        return None

def parse_firmographic_data(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        address = soup.find('address')
        if address:
            return address.get_text(strip=True)
        else:
            raise ValueError("Address not found")
    except Exception as e:
        logging.error(f"Error parsing firmographic data: {e}")
        raise

def handle_dynamic_content(url):
    try:
        service = Service(CHROME_DRIVER_PATH)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        dynamic_content = driver.page_source
        driver.quit()
        return dynamic_content
    except TimeoutException:
        logging.error(f"Timeout while handling dynamic content for {url}")
        raise
    except Exception as e:
        logging.error(f"Error handling dynamic content: {e}")
        raise

def solve_captcha(captcha_image):
    try:
        image = Image.open(captcha_image)
        captcha_solution = pytesseract.image_to_string(image)
        return captcha_solution.strip()
    except Exception as e:
        logging.error(f"Error solving CAPTCHA: {e}")
        raise

def store_data(firmographic_data):
    try:
        with open('firmographic_data.json', 'a') as f:
            json.dump(firmographic_data, f)
            f.write('\n')
        return True
    except Exception as e:
        logging.error(f"Error storing data: {e}")
        return False

def main():
    for url in company_urls:
        try:
            html_content = fetch_webpage(url)
            if html_content is None:
                continue

            if "CAPTCHA" in html_content:
                captcha_solution = solve_captcha('/path/to/captcha/image')
                # Logic to submit CAPTCHA solution and retry fetching the page
                continue

            if "dynamic content" in html_content:
                html_content = handle_dynamic_content(url)

            firmographic_data = parse_firmographic_data(html_content)
            if firmographic_data:
                store_data(firmographic_data)

        except TimeoutException:
            logging.info("Retrying after timeout...")
            time.sleep(5)
            continue
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            continue

if __name__ == "__main__":
    main()
```
