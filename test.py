from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from pkgutil import iter_importers
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

from requests.exceptions import ProxyError, SSLError, ConnectTimeout
import requests

def set_driver(url):
    """
    Set up the chrome driver.
    :return: Chrome driver for which setup is completed.
    :rtype:<class 'selenium.webdriver.chrome.webdriver.WebDriver'>
    """
    webdriver_options = webdriver.ChromeOptions()
    # webdriver_options.add_argument('headless')
    webdriver_options.add_argument('disable-gpu')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver_options)
    driver.get(url=url)
    return driver


def set_select_box(driver):
    """
    Set the select value of "www.spys.one/en/https-ssl-proxy/" to 500
    :param driver: Chrome driver for which setup is completed.
    """

    select = Select(driver.find_element_by_name("xpp"))
    select.select_by_visible_text('500')
    select = Select(driver.find_element_by_name("xpp"))
    select_option = select.first_selected_option.text

    if select_option != '500':
        print("다시 시도합니다.")
        set_select_box(driver)
    
    # print(f"셀렉트 옵션:{select_option}")


def get_proxy_list():
    """
    Gets the IP and address of the proxy.
    :return: The ip and address of the proxies
    :rtype: list
    """
    proxy_list = []
    trs = soup.select("tr[onmouseover]")
    url = 'https://www.google.com'
    for cnt, tr in enumerate(trs):
        proxy_server = tr.select_one("font.spy14").text
        if proxy_server is not None:
            proxy_list.append(proxy_server)    
        else:
            print(f"index:{cnt} 프록시 서버를 얻어오지 못했습니다.")
            continue
    return proxy_list
        

if __name__ == "__main__":


    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "content-type": "application/json",
    }
    url = 'https://spys.one/en/https-ssl-proxy/'

    
    chrome_driver = set_driver(url)     # 드라이버 셋팅: 수정해도 상관없음
    set_select_box(chrome_driver)       # 

    html = chrome_driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    proxy_list = get_proxy_list()
    print(proxy_list)

    while True:
        if len(proxy_list) == 0:
            proxy_list = get_proxy_list()
        for cnt, proxy in enumerate(proxy_list):
            proxies = {"http": proxy, 'https': proxy}
            print(f'proxies: {proxies}')

            resp = requests.get(url, headers=headers, proxies=proxies, timeout=5)
            print(resp.status_code)
            # try:
            #     resp = requests.get(url, headers=headers, proxies=proxies, timeout=5)

            # except (ProxyError, SSLError, ConnectTimeout, ConnectionError) as e:        
            #     proxy_list.remove(proxy)
            #     print(f'proxy len: {len(proxy_list)}')
            #     continue

            # print(f"{proxy} 정상적으로 저장")


    # print(proxy_list)
    chrome_driver.quit()
