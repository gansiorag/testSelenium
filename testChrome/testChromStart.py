import sys, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from termcolor import cprint
from termcolor import colored
from time import sleep

file_dir = os.path.dirname(__file__)
print(file_dir)
sys.path.append(file_dir.split('testSelenium')[0] + 'testSelenium')
options_chr= Options()
vis = 'n'
if vis != 'v': 
    options_chr.headless = False
    #options_chr.add_argument('--headless')
    #options_chr.headless = True
    #options_chr.add_argument(f"user-agent={customUserAgent}")
    #options_chr.add_argument('--disable-gpu')
    # options_chr.add_argument('--remote-debugging-port=9222')
    # options_chr.add_argument('--enable-javascript')
    # options_chr.add_argument('--no-sandbox')
    # options_chr.add_argument('--window-size= 1920,1080')
    # options_chr.add_argument("--disable-extensions")
    # options_chr.add_argument("--proxy-server='direct://'")
    # options_chr.add_argument("--proxy-bypass-list=*")
    # options_chr.add_argument("--start-maximized")
    # options_chr.add_argument('--disable-dev-shm-usage')
    # options_chr.add_argument('--ignore-certificate-errors')
    # options_chr.add_argument('--allow-running-insecure-content')
    # options_chr.add_argument('--allow-insecure-localhost')
    # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    # options_chr.add_argument(f'user-agent={user_agent}')
    #options_chr.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')

    fileDriver ='/home/gansiorag/MyParth/ProjectMy/testSelenium/testChrome/chromedriver/chromedriver_107_0_5304_62'
    #fileDriver ='/home/gansiorag/MyParth/ProjectMy/testSelenium/testChrome/chromedriver/chromedriver_107_0_5304_18'
    global driver
    driver = webdriver.Chrome(executable_path=fileDriver,chrome_options=options_chr)

    driver.maximize_window()
    driver.get("https://dzen.ru/?yredirect=true")
    sleep(1)
    textEnter=driver.find_element(By.XPATH,"""//div[@class="card-news__header-uD"]""")
    textLiA=driver.find_elements(By.XPATH,"""//div[@class="card-news__header-uD"]//a""")
    for aa in textLiA:
        print(aa.get_attribute('href'))
    sleep(30)