import requests
from selenium import webdriver
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urljoin
import time


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
        print(e)

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
        print(e)


if __name__ == "__main__":
    user = input("유저명 : ")
    wasm(user)
    redSecurity(user)
    print(forum)
    print(errorForum)
