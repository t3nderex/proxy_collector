from ast import MatchMapping, main
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium import webdriver


def get_proxies():
    options = webdriver.ChromeOptions()
    options.add_argument("log-level=3")
    options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
        chrome_options=options)
    driver.get("https://free-proxy-list.net/")

    PROXIES = []
    tbody = driver.find_element(By.XPATH, "//*[@id=\"list\"]/div/div[2]/div/table/tbody")
    trs = tbody.find_elements(By.TAG_NAME, 'tr')
    print(len(trs))
    for tr in trs:
        ip = tr.find_element(By.TAG_NAME,"td")
        try:
            PROXIES.append(ip.text)
        except:
            print("IP를 가져오지 못함")
    driver.close()

    if len(PROXIES) < 1:
        print("--- Proxies used up (%s)" % len(PROXIES))
        PROXIES = get_proxies()
    print(PROXIES)

    return PROXIES
    


if __name__ == '__main__':
    proxies = get_proxies()
    with open('proxy_list.txt', "w") as f:
        for proxy in proxies:
            f.write(proxy)
        
        
    