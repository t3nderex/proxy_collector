from bs4 import BeautifulSoup
from numpy import isin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


def set_driver(driver_path, url):
    """
    Set up the chrome driver.
    :return: Chrome driver for which setup is completed.
    :rtype:<class 'selenium.webdriver.chrome.webdriver.WebDriver'>
    """
    webdriver_options = webdriver.ChromeOptions()
    # webdriver_options.add_argument('headless')
    webdriver_options.add_argument('disable-gpu')
    driver = webdriver.Chrome(service=Service(executable_path = driver_path), options=webdriver_options)
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
    
    print(f"셀렉트 옵션:{select_option}")


def get_proxy_list():
    """
    Gets the IP and address of the proxy.
    :return: The ip and address of the proxies
    :rtype: list
    """
    proxy_list = []
    trs = soup.select("tr[onmouseover]")
    for tr in trs:
        e_ip = tr.select_one("font.spy14")  # ip
        if e_ip is not None:
            for item in e_ip.findAll('script'):         # 포트 찾기
                item.extract()
            ip = e_ip.text
        else:
            continue

        proxy_list.append(ip)
    return proxy_list
        
    
if __name__ == "__main__":

    driver_path = 'tools/proxy/chromedriver'
    url = 'https://spys.one/en/https-ssl-proxy/'

    
    chrome_driver = set_driver(driver_path, url)
    set_select_box(chrome_driver)

    html = chrome_driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    proxy_list = get_proxy_list()

    # print(f"프록시 리스트:{proxy_list}")
    
    with open("tools/proxy/proxy_list.txt", "w", encoding="utf-8") as f:
        f.writelines(f"{proxy}\n" for proxy in proxy_list)

    print(proxy_list)
    chrome_driver.quit()
