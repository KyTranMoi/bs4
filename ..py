from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

# Khởi tạo trình duyệt (ở đây sử dụng Chrome)
driver = webdriver.Chrome('chromedriver.exe')

# Mở trang web
driver.get("https://hashnode.com/n/machine-learning")
time.sleep(2)
# Lấy vị trí cuộn trang ban đầu
last_position = driver.execute_script("return window.pageYOffset;")

while True:
    # Cuộn trang xuống dưới
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    
    # Đợi 1 giây để trang cuộn xuống
    time.sleep(1)
    
    # Lấy vị trí cuộn trang hiện tại
    current_position = driver.execute_script("return window.pageYOffset;")
    
    # Kiểm tra nếu vị trí cuộn trang không thay đổi, tức đã cuộn đến cuối trang
    if last_position == current_position:
        break
    
    # Cập nhật vị trí cuộn trang cuối cùng
    last_position = current_position

# Đóng trình duyệt
list_link = []
links=driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/main/div[2]/div[2]/div/div[2]/div[1]/h1/a')
list_link = [i.get_attribute("href") for i in links]
print(list_link)
driver.quit()
