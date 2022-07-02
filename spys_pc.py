from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

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
<<<<<<< HEAD
=======

>>>>>>> f53c08a951818d2f9fc0cccd88838e97004222dd
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
    return True

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

    url = 'https://spys.one/en/https-ssl-proxy/'

    
<<<<<<< HEAD
    chrome_driver = set_driver(url)
    set_select_box(chrome_driver)
=======
    driver = set_driver(driver_path, url)
    driver.implicitly_wait(3)
    set_select_box(driver)
>>>>>>> f53c08a951818d2f9fc0cccd88838e97004222dd

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    proxy_list = get_proxy_list()
    
<<<<<<< HEAD
    with open("proxy_list.txt", "w", encoding="utf-8") as f:
=======
    with open("./proxy_list.txt", "w", encoding="utf-8") as f:
>>>>>>> f53c08a951818d2f9fc0cccd88838e97004222dd
        f.writelines(f"{proxy}\n" for proxy in proxy_list)

    print(proxy_list)
    driver.quit()
