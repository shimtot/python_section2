import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
#Rest : POST, GET, PUT:UPDATE, REPLACE(FETCH:UPDATE, MODIFY), DELETE

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless") #CLI

DRIVER = webdriver.Chrome(chrome_options=chrome_options,executable_path='c:/Django/workspace/section3/webdirver/')
#driver = webdriver.PhantomJS('c:/Django/workspace/section3/webdirver/phantomjs/phantomjs')
#driver.set_window_size(1920,1280)
#driver.implicitly_wait(5)
driver.get('https://google.com')
time.sleep(5)
driver.save_screenshot("c:/Django/test/website1.jpg")

#driver.implicitly_wait(5)
driver.get('https://daum.net')
time.sleep(5)
driver.save_screenshot("c:/Django/test/daum.jpg")

driver.quit()
print('스크린샵 완료')
