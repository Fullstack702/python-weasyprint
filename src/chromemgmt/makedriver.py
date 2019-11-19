from selenium import webdriver
import os

from chromemgmt.chromepaths import headless_chrome_path, chromedriver_path

data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'chrome-data'))



def make_chrome_driver() -> webdriver.Chrome:
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--window-size=1280x1696')
	chrome_options.add_argument(f'--user-data-dir={data_path}/user-dir')
	chrome_options.add_argument('--hide-scrollbars')
	chrome_options.add_argument('--enable-logging')
	chrome_options.add_argument('--log-level=0')
	chrome_options.add_argument('--v=99')
	chrome_options.add_argument('--single-process')
	chrome_options.add_argument(f'--data-path={data_path}/data-dir')
	chrome_options.add_argument('--ignore-certificate-errors')
	chrome_options.add_argument(f'--homedir={data_path}/home-dir')
	chrome_options.add_argument(f'--disk-cache-dir={data_path}/cache-dir')
	chrome_options.binary_location = headless_chrome_path

	driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)
	return driver
