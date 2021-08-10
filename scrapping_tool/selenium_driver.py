
from selenium import webdriver
import chromedriver_autoinstaller

# check if chrome driver has same version as browser
chromedriver_autoinstaller.install()

# add otions to driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

#driver = webdriver.Chrome("C:/Users/dandei/Desktop/SlackBot/slack_bot/chromedriver_win32/chromedriver.exe", chrome_options=options)
driver = webdriver.Chrome(chrome_options=options)