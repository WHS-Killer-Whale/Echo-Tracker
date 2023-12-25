import requests
from bs4 import BeautifulSoup

# UI 관련 내용입니다.
from pyfiglet import Figlet
from clint.textui import colored

f = Figlet(font="slant")
print(
    colored.white(
        "---------------------------------------------------------------------------"
    )
)
print(f.renderText("Whats My Name"))
print(
    colored.white(
        "----------------------------------------------------------KILLER WHALE _whs"
    )
)

proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

# 전역 변수와 공통 함수 입니다.
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

def dark2web(user):
    url = "https://web-1.gate2dark.online"
    name = 'dark2web'
    try:
        response = requests.get(url)
        cookies = response.cookies
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        element = soup.find(id='XF')
        data_csrf = element['data-csrf']
        url = 'https://web-1.gate2dark.online/index.php?members/find&_xfRequestUri=%2Fmembers%2F&_xfWithData=1&_xfResponseType=json&_xfToken='+data_csrf+'&q='+user
        response = requests.post(url, cookies=cookies)
        json_data = response.json()
        for item in json_data['results']:
            id_value = item['id']
            if id_value.lower() == user.lower():
                userID = item['iconHtml'].split('data-user-id="')[1].split('"')[0]
                userStatus(True, f"{name}(userID: {userID})")
    except Exception as e:
        notSearch(name)

if __name__ == "__main__":
    user = input("USER NAME : ")
    dark2web(user)

    print(colored.green("\n>>> DETECTED: "))
    for i in forum:
        print("\t" + i)

    print(colored.red("\n>>> unknown: ", errorForum))
    for i in errorForum:
        print("\t" + i)

