from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# initialize Chrome driver
driver = webdriver.Chrome()
driver.get('https://www.airbnb.com/rooms/39663644?category_tag=Tag%3A8099&check_in=2023-01-31&check_out=2023-02-01&source_impression_id=p3_1677139635_i4vGet1KX8CXouAd')

WAIT_TIME = 60

# find and click the button to open the reviews popup
button_text = 'Show all 142 reviews'
button = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, '')))
button.click()
time.sleep(10)
# wait for the popup to load
popup = WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((By.XPATH, "")))

# scroll to the bottom of the popup to load all reviews
while True:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
    time.sleep(1)
    new_height = driver.execute_script('return arguments[0].scrollHeight', popup)
    if new_height == last_height:
        break
    last_height = new_height

# parse the HTML of the popup using BeautifulSoup
soup = BeautifulSoup(popup.get_attribute('innerHTML'), 'html.parser')
reviews = soup.select('div[data-testid="reviews-container"] div[data-testid="expanded-review"]')

# extract the relevant information from each review and print it
for review in reviews:
    name = review.select_one('div[data-testid="reviews-user-details"] span').get_text(strip=True)
    date = review.select_one('div[data-testid="reviews-user-details"] time').get('datetime')
    comment = review.select_one('div[data-testid="expanded-review-content"]').get_text(strip=True)
    rating = review.select_one('div[data-testid="reviews-rating"] span').get_text(strip=True)
    print(f'{name} ({date}): {comment}\nRating: {rating}\n')
    
# close the driver
driver.quit()
