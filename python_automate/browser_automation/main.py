# type: ignore
from pathlib import Path
import time

from datetime import datetime as dt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# # Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# # Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / "drivers" / "chromedriver"


def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-dev-shm-usage")
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("disable-blink-features=AutomationControlled")

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def write_file(text):
    """Write input text into a text file"""
    filename = f"{dt.now().strftime('%Y-%m-%d, %H-%M-%S')}.txt"
    with open(filename, "w") as file:
        file.write(text)


def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys(
        "automatedautomated" + Keys.RETURN
    )
    time.sleep(2)

    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)

    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
    element = str(clean_text(element))
    write_file(element)
    return clean_text(element)


print(main())
