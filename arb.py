from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.service import Service as EdgeService

driver = EdgeService(executable_path="msedgedriver.exe" )

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)


options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46' )

driver = webdriver.Edge(options=options)

WAIT_TIME = 60

driver.get('https://www.airbnb.com/rooms/39663644?category_tag=Tag%3A8099&check_in=2023-01-31&check_out=2023-02-01&source_impression_id=p3_1677139635_i4vGet1KX8CXouAd')
driver.maximize_window()

# temukan tombol "Show all" pada lokasi pop-up dan klik
WAIT_TIME = 60
location_button = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/section/div[2]/div[1]/span[1]/span[3]/button')))
location_button.click()

# location_button = driver.find_element_by_xpath("//button[contains(text(), '142 reviews')]")
# location_button.click()

# tunggu sampai pop up muncul
WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_14vzertx']")))



# lakukan loop untuk mengambil semua data dari pop up
while True:
    # ambil semua elemen dari lokasi
    locations = driver.find_element(By.CLASS_NAME, '_17itzz4')

    # locations = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_17itzz4']")))
    # locations = driver.find_elements_by_xpath("//div[@class='_1ruvvry']//div[@class='_17itzz4']")
    # for location in locations:
    #     print(location.text)

    # coba untuk scroll ke bawah
    try:
        # cari elemen terakhir pada pop up
        last_location = locations[-1]
        # scroll ke elemen terakhir
        actions = ActionChains(driver)
        actions.move_to_element(last_location).perform()
        # tunggu beberapa detik untuk memuat data baru
        time.sleep(30)
    except:
        break

# tutup driver setelah selesai
driver.quit()
