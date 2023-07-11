import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_FOLDER = Path(__file__).parent


CHROMEDRIVER_EXEC = ROOT_FOLDER / 'driver' / 'chromedriver'


chorme_options = webdriver.ChromeOptions()
chorme_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
chorme_browser = webdriver.Chrome(
    service=chorme_service,
    options=chorme_options,
)

chorme_browser.get("https://www.google.com.br")
time.sleep(5)
