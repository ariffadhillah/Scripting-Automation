from selenium import webdriver
import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Inisialisasi driver
import time
driver = webdriver.Chrome()
WAIT_TIME = 60
# Buka halaman web
time.sleep(3)
driver.get("https://www.cdph.ca.gov/Programs/CHCQ/LCP/CalHealthFind/Pages/Complaint.aspx?facid=630021163")
driver.implicitly_wait(60)
element = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.ID, 'id="lblDistrictInfo"')))
# Temukan elemen HTML
# element = driver.find_element("#lblDistrictInfo.value.notranslate")

# Pisahkan data dalam elemen menjadi beberapa bagian
data = element.text.split("\n")

# Cari section yang sesuai dengan data yang ingin diambil
section_name = "L&C District Office Information"
section_index = data.index(section_name)

# Ambil data pada section yang sesuai
district_office_info = data[section_index+1:section_index+5]

# Buat file Excel baru
wb = openpyxl.Workbook()
sheet = wb.active

# Simpan data dalam kolom Excel yang berbeda
sheet["A1"] = district_office_info[0]
sheet["B1"] = district_office_info[1]
sheet["C1"] = district_office_info[2]
sheet["D1"] = district_office_info[3]

# Simpan file Excel
wb.save("data.xlsx")

# Tutup browser
driver.quit()
