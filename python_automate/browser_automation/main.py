# type: ignore
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# # Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# # Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / "drivers" / "chromedriver.exe"

print(CHROME_DRIVER_PATH)


def get_driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("disable-infobars")
    # chrome_options.add_argument("start-maximized")
    # chrome_options.add_argument("disable-dev-shm-usage")
    # chrome_options.add_argument("no-sandbox")
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # chrome_options.add_argument("disable-blink-features=AutomationControlled")

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get("https://mangalivre.net/")
    return driver


driver = get_driver()
element = driver.find_element(by="xpath", value="/html/body/div[1]")


print(element.text)
