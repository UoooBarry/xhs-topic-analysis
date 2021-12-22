import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

descriptions = []
comments = []
LIMIT = 300

chrome = Service(ChromeDriverManager().install())

def get_detail(id):
    url = "https://www.xiaohongshu.com/discovery/item/" + id
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--window-size=1920,1080")
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(service=chrome, options=options)

    driver.get(url)
    try:
        description = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "content")))
        if description:
            for comment in description[1::]:
                comments.append([id, comment.text])

            description = description[0].text
        else: 
            description = ""
        driver.quit()
    except TimeoutException:
        description = "--Time out!--"
        driver.get_screenshot_as_file("./out/screenshots/screenshot-" + str(id)  +".png")
        driver.quit()

    print(description)
    print()
    return description


csvfile = open('./out/小红书.csv', 'r')
ids = ([x[0] for x in csv.reader(csvfile)])

for i, id in enumerate(ids):
    print(str(i + 1) + ': ' + id)
    descriptions.append(get_detail(id))

with open('./out/小红书.csv', 'r') as read_obj, \
        open('./out/小红书_笔记.csv', 'w', newline='') as write_obj:
    # Create a csv.reader object from the input file object
    csv_reader = csv.reader(read_obj)
    # Create a csv.writer object from the output file object
    csv_writer = csv.writer(write_obj)
    # Read each row of the input csv file as list
    for i, row in enumerate(csv_reader):
        # Append the default text in the row / list
        row.append(descriptions[i])
        # Add the updated row / list to the output file
        csv_writer.writerow(row)

f = open('./out/小红书_笔记_评论.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(f)
for comment in comments:
    csv_writer.writerow(comment)
