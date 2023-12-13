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
       
def hostingforums(user):
    url = "https://hostingforums.net/u/"
    name = 'hostingforums'
    userUrl = url + user
    try :
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except :
        notSearch(name)

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
            userStatus(found, name)
    except Exception as e:
        print(e)
        notSearch(name)

def wilderssecurity(user):
    url = "https://www.wilderssecurity.com/search/search"
    name = 'wilderssecurity'
    payload = {
        "keywords": "",
        "users": user,
        "date": "",
        "_xfToken": ""}
    try :
        response = requests.post(url, headers=headers, data=payload)
        if 'The following members could not be found' not in response.text:
            userStatus(True, name)
    except :
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
        hostingforums(user)
        landzdown(user)
        wilderssecurity(user)

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
