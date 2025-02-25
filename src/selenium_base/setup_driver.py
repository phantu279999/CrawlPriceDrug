from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# auto download chromedriver
chromedriver_autoinstaller.install()


def custom_chrome():
	options_chrome = Options()
	options_chrome.page_load_strategy = "eager"
	options_chrome.add_argument("--start-maximized")
	options_chrome.add_experimental_option('excludeSwitches', ['enable-logging'])

	driver = webdriver.Chrome(options=options_chrome)

	driver.implicitly_wait(30)

	return driver


def custom_chrome_headless():
	options_chrome = Options()
	options_chrome.page_load_strategy = "eager"
	options_chrome.add_argument("--start-maximized")
	options_chrome.add_argument("--headless")
	# options_chrome.add_argument('--ignore-certificate-errors')
	# options_chrome.add_argument('--ignore-ssl-errors')
	options_chrome.add_argument('--disable-extensions')
	# options_chrome.add_argument('--no-sandbox')
	options_chrome.add_argument('--disable-dev-shm-usage')
	# options_chrome.add_argument('--incognito')
	# options_chrome.add_argument("--disable-background-networking")
	options_chrome.add_argument("--disable-notifications")
	options_chrome.add_argument('--disable-infobars')
	options_chrome.add_experimental_option('excludeSwitches', ['enable-logging'])

	driver = webdriver.Chrome(options=options_chrome)
	driver.implicitly_wait(30)

	return driver
