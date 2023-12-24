import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urljoin
import time

# UI 관련 내용입니다.
from pyfiglet import Figlet
from clint.textui import colored

f = Figlet(font='slant')
print(colored.white("---------------------------------------------------------------------------"))
print(f.renderText('Whats My Name'))
print(colored.white("----------------------------------------------------------KILLER WHALE _whs"))


proxies = {"http": "socks5h://localhost:9050", "https": "socks5h://localhost:9050"}

# 전역 변수와 공톰 함수 입니다.
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}
forum = []
errorForum = []


def userStatus(Bool, name):
    if Bool:
        forum.append(name)


def notSearch(name):
    errorForum.append(name)


# 여기서 부터 작성하세요
def _0Day(user):
    url = "https://0day.red/"
    name = '0Day'
    userUrl = url + 'User-' + user
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except :
        notSearch(name)


def _0x00sec(user):
    url = "https://0x00sec.org/"
    name = '0x00sec'
    userUrl = url + 'u/' + user
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except:
        notSearch(name)
        

def _1877(user):
    url = "https://1877.to/forums/"
    name = '1877'
    userUrl = url + user + '/'
    try:
        response = requests.get(userUrl, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        body = soup.body
        if body and 'data-template' in body.attrs:
            data_template_value = body['data-template']
            if data_template_value == 'member_view':
                userStatus(True, name)
            elif data_template_value == 'error':
                userStatus(False, name)
    except:
        notSearch(name)

def wasm(user):
    url = "https://wasm.in/index.php?members/find"
    name = "Wasm.in"
    payload = {
        "q": user,
        "_xfRequestUri": "/",
        "_xfNoRedirect": 1,
        "_xfResponseType": "json"
    }
    try:
        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200 and user in response.json().get("results", {}):
            userStatus(True, name)

    except Exception as e:
        notSearch(name)

def redSecurity(user):
    url = "https://redsecurity.info/cc/xmlhttp.php?action=get_users"
    name = "RedSecurity"
    timestamp = int(time.time() * 1000)
    payload = {
        "query": user,
        "_": timestamp
    }
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if result and user == result[0].get("id"):
                userStatus(True, name)

    except Exception as e:
        notSearch(name)

def ramble(user):
    name = "ramble"
    url = (
        "http://rambleeeqrhty6s5jgefdfdtc6tfgg4jj6svr4jpgk4wjtg3qshwbaad.onion/user/"
        + user
    )
    try:
        response = requests.get(url, proxies=proxies)
        if response.status_code == 200:
            userStatus(True, name)
        else:
            pass
    except:
        notSearch(name)

def R0CREW(user):
    url = 'https://forum.reverse4you.org/'
    name = 'R0CREW'
    userUrl = url + 'u/' + user + '/summary'
    try :
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except :
        notSearch(name)
        
        
def hack5(user):
    url = 'https://forums.hak5.org/search/?&q='
    name = 'hack5'
    userUrl = url + user + '&type=core_members&quick=1&joinedDate=any&group[10]=1'
    try:
        response = requests.get(userUrl, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        if 'Found 0 results' not in soup.text:
            userStatus(True, name)
    except :
        notSearch(name)

def rootme(user):
    url = 'https://www.root-me.org/'
    name = 'rootme'
    userUrl = url + user
    try :
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 304:
            userStatus(True, name)
    except :
        notSearch(name)

<<<<<<< Updated upstream
=======
def landzdown(user):
    url = "https://www.landzdown.com/index.php?action=mlist;sa=search"
    name = 'landzdown'
    payload = {
        'search': user,
        'fields[]': 'name',
        'submit': 'Search'
    }
    try:
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.find_all('td', class_='real_name lefttext')
            found = any(row.get_text(strip=True) == user for row in rows)

            user_link = soup.find('a', title=f'View the profile of {user}')
            
            if user_link:
                user_url = user_link['href']
                user_id = user_url.split('=')[-1]
                userStatus(True, name + f"(userID: {user_id})")
    except Exception as e:
        print(e)
        notSearch(name)
>>>>>>> Stashed changes


def infectedzone(user):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    url = "https://infected-zone.com/search/"
    name = 'InfectedZone'
    driver.get(url)
    time.sleep(3)
    search_elem = driver.find_element(
        By.CSS_SELECTOR,
        "#top > div.p-body > div > div > div > div > div > form > div > div > dl:nth-child(2)",
    )
    search_elem = search_elem.find_element(By.NAME, "c[users]")
    search_elem.send_keys(user)

    submit = driver.find_element(
        By.CSS_SELECTOR,
        "#top > div.p-body > div > div > div > div > div > form > div > dl > dd > div > div.formSubmitRow-controls > button",
    )
    submit.submit()
    time.sleep(3)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    user_link = soup.find('a', class_='username')
    if user_link:
        data_user_id = user_link.get('data-user-id')
        userStatus(True, name + f"(userID: {data_user_id})")
    else:
        notSearch(name)
    driver.close()

    

if __name__ == "__main__":
<<<<<<< Updated upstream
	while(True):
		user = input(colored.blue("USER NAME: "))
		_0Day(user)
		_0x00sec(user)
		_1877(user)
		wasm(user)
		redSecurity(user)
		ramble(user)
    R0CREW(user)
    hack5(user)
    rootme(user)
=======
    while(True):
        user = input(colored.blue("USER NAME: "))
        _0Day(user)
        _0x00sec(user)
        _1877(user)
        wasm(user)
        redSecurity(user)
        ramble(user)
        R0CREW(user)
        hack5(user)
        rootme(user)
        bhcforums(user)
        enclavecc(user)
        nullbb(user)
        hostingforums(user)
        landzdown(user)
        wilderssecurity(user)
        infectedzone(user)
>>>>>>> Stashed changes

		print(colored.green("\n>>> DETECTED: "))
		for i in forum:
			print("\t" + i)

		print(colored.red("\n>>> unknown: ", errorForum))
		for i in errorForum:
			print("\t" + i)

		print('\n')
		print(colored.white("----------------------------------------------------------KILLER WHALE _whs"))

		# clear list
		forum.clear()
		errorForum.clear()


    