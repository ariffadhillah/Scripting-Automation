from selenium import webdriver
from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# driver = ChromeService(executable_path="chromedriver.exe" )
driver = EdgeService(executable_path="msedgedriver.exe" )

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)


options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46' )

driver = webdriver.Edge(options=options)

WAIT_TIME = 60

driver.get('https://www.airbnb.com/rooms/39663644?category_tag=Tag%3A8099&check_in=2023-01-31&check_out=2023-02-01&source_impression_id=p3_1677139635_i4vGet1KX8CXouAd')
driver.maximize_window()


# klik tombol untuk membuka pop up
button = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/section/div[2]/div[1]/span[1]/span[3]/button')))
button.click()

# menuggu pop up muncul
popup = WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, '_17itzz4')))

while True:
    # hitung ketinggian pop up
    height = driver.execute_script("return arguments[0].scrollHeight", popup)
    time.sleep(2)
    # scroll ke bawah
    driver.execute_script(f"arguments[0].scrollTo(0, {height});", popup)
    try:
        time.sleep(.5)
    except:
       break
# menutup pop up
close_button = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']")))
close_button.click()

driver.quit()




