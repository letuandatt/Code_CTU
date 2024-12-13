import pandas as pd
import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# Cấu hình driver
service = Service("C:/Users/LE TUAN DAT/.wdm/drivers/chromedriver/win64/130.0.6723.91/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
url = "https://s.cafef.vn/lich-su-giao-dich-fpt-1.chn#data"

# Mở trang
driver.get(url)
wait = WebDriverWait(driver, 10)

input_date = driver.find_element(By.CSS_SELECTOR, 'input[name="daterange"]')
input_date.clear()
input_date.send_keys("01/01/2014 - 01/11/2024")
input_date.send_keys(Keys.ENTER)

view_btn = driver.find_element(By.CSS_SELECTOR, "#owner-find")
view_btn.click()

time.sleep(2)

data = []
while True:
    try:
        disabled_elements = driver.find_elements(By.CSS_SELECTOR, 'i[class="fa fa-chevron-right enable"]')

        element = driver.find_element(By.CSS_SELECTOR, "#divStart > div > div.wraper-pagination > div:nth-child(3)")

        # Lấy nội dung trang và phân tích với BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Tìm bảng dữ liệu
        table = soup.find('tbody', {'class': 'render-table-owner'})
        rows = table.find_all("tr")

        # Lấy từng dòng
        for row in rows:
            cols = row.find_all("td")
            data.append({
                "Ngày": cols[0].text,
                "Giá mở": cols[8].text,
                "Giá cao nhất": cols[9].text,
                "Giá thấp nhất": cols[10].text,
                "Giá đóng": cols[1].text,
                "Giá điều chỉnh": cols[2].text,
                "Giá trị thay đổi": re.sub(r'\(.*\)', '', cols[3].text).strip(),
                "% thay đổi": re.search(r'\(([^%]+)%\)', cols[3].text).group(1).strip(),
                "Tổng KL GD": cols[4].text,
                "Tổng GT GD": cols[5].text,
            })

        if disabled_elements:
            break
        element.click()

        time.sleep(1)

    except Exception as e:
        print("Có lỗi xảy ra:", e)
        break

df = pd.DataFrame(data)
df.to_csv("du_lieu_FPT4.csv")
print(df)

driver.quit()

