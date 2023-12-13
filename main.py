import requests
# from selenium import webdriver
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

def bhcforums(user):
    query_params = {
        'action': 'get_users',
        'query': user,
    }
    url = "https://bhcforums.cc/xmlhttp.php"
    name = 'bhcforums.cc'
    query_string = urlencode(query_params)
    userUrl = f"{url}?{query_string}"
    
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            
            for user_info in json_data:
                if 'id' in user_info and user_info['id'] == f"{user}":
                    userStatus(True, name)
                    break
    except:
        notSearch(name)

def enclavecc(user):
    query_params = {
        'q': user,
        'type': 'core_members',
        'joinedDate': 'any',
        'group[4]': '1',
        'group[19]': '1',
        'group[9]': '1',
        'group[12]': '1',
        'group[22]': '1',
        'group[6]': '1',
        'group[3]': '1',
        'group[7]': '1',
        'group[18]': '1',
        'group[23]': '1',
        'group[20]': '1',
        'group[21]': '1',
        'group[14]': '1',
        'group[15]': '1',
        'group[16]': '1',
        'group[10]': '1',
    }
    url = "https://www.enclave.cc/index.php"
    name = 'enclave.cc'
    query_string = urlencode(query_params)
    userUrl = f"{url}?/search/&{query_string}"
    
    try:
        response = requests.get(userUrl, headers=headers)
        if 'There were no results for your search. Try broadening your criteria or choosing a different content area.' in response.text:
            pass
        elif response.status_code == 200:
            if (f"Go to {user}'s profile") in response.text:
                userStatus(True, name)
    except:
        notSearch(name)
    time.sleep(2)

def nullbb(user):
    query_params = {
        'action': 'get_users',
        'query': user,
    }
    url = "https://nulledbb.com/xmlhttp.php"
    name = 'nullBB.com'
    query_string = urlencode(query_params)
    userUrl = f"{url}?{query_string}"
    
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            
            found = False
            for user_info in json_data:
                if 'id' in user_info and str(user_info['id']).lower() == user.lower():
                    userStatus(True, name)
                    found = True
                    break
    except:
        notSearch(name)

if __name__ == "__main__":
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


    