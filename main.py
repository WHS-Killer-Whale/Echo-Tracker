import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urljoin
import time
import re

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
def breachForums(user):
    name = "breachForums"
    url = "http://breachedu76kdyavc6szj6ppbplfqoz3pgrk3zw57my4vybgblpfeayd.onion"
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        cookies = response.cookies
        url = "http://breachedu76kdyavc6szj6ppbplfqoz3pgrk3zw57my4vybgblpfeayd.onion/User-"
        userUrl = url + user
        response = requests.get(
            userUrl, headers=headers, proxies=proxies, cookies=cookies
        )
        if response.text.find("The member you specified is either") == -1:
            userStatus(True, name)
    except Exception as e:
        notSearch(name)


def _0Day(user):
    url = "https://0day.red/"
    name = "0Day"
    userUrl = url + "User-" + user
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except:
        notSearch(name)


def _0x00sec(user):
    url = "https://0x00sec.org/"
    name = "0x00sec"
    userUrl = url + "u/" + user
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except:
        notSearch(name)


def _1877(user):
    url = "https://1877.to/forums/search/"
    name = "1877"

    paylaod = {
        "keywords": "",
        "c[users]": user,
        "c[newer_than]": "",
        "c[older_than]": "",
        "order": "date",
        "search_type": "",
    }

    try:
        response = requests.get(url, headers=headers)
        cookies = response.cookies
        soup = BeautifulSoup(response.text, "html.parser")
        body = soup.body
        form = body.find("form")
        find_token = form.find("input", {"name": "_xfToken"})
        token = find_token["value"]

        paylaod["_xfToken"] = token

        response = requests.post(
            url + "search", headers=headers, data=paylaod, cookies=cookies
        )
        soup = BeautifulSoup(response.text, "html.parser")
        body = soup.body
        if body and "data-template" in body.attrs:
            data_template_value = body["data-template"]
            if data_template_value == "search_results":
                find_user_id = body.find("a", class_="username")
                user_id = find_user_id.get("data-user-id")
                userStatus(True, name + f"(userID: {user_id})")
            elif data_template_value == "error":
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
        "_xfResponseType": "json",
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
    payload = {"query": user, "_": timestamp}
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if result and user == result[0].get("id"):
                userid = result[0].get("uid")
                userStatus(True, name + f"(userID: {userid})")

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
    url = "https://forum.reverse4you.org/"
    name = "R0CREW"
    userUrl = url + "u/" + user + "/summary"
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except:
        notSearch(name)


def hack5(user):
    url = "https://forums.hak5.org/search/?&q="
    name = "hack5"
    userUrl = url + user + "&type=core_members&quick=1&joinedDate=any&group[10]=1"
    try:
        response = requests.get(userUrl, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        if "Found 0 results" not in soup.text:
            userStatus(True, name)
    except:
        notSearch(name)


def rootme(user):
    url = "https://www.root-me.org/"
    name = "rootme"
    userUrl = url + user
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 304:
            userStatus(True, name)
    except:
        notSearch(name)


def hostingforums(user):
    url = "https://hostingforums.net/u/"
    name = "hostingforums"
    userUrl = url + user
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except:
        notSearch(name)


def megatop(user):
    url = "https://megatop.biz/forum/"
    name = "megatop"
    try:
        response = requests.get(url, headers=headers)
        cookies = response.cookies
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        element = soup.find(id="XF")
        data_csrf = element["data-csrf"]
        url = (
            "https://megatop.biz/index.php?members/find&&_xfRequestUri=%2Fforum%2F&_xfWithData=1&_xfToken="
            + data_csrf
            + "&_xfResponseType=json&q="
            + user
        )
        response = requests.get(url, headers=headers, cookies=cookies)
        json_data = response.json()
        for item in json_data["results"]:
            id_value = item["id"]
            if id_value.lower() == user.lower():
                userStatus(True, name)
    except Exception as e:
        notSearch(name)


def dark2web(user):
    url = "https://web-1.gate2dark.online/"
    name = "dark2web"
    try:
        response = requests.get(url)
        cookies = response.cookies
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        element = soup.find(id="XF")
        data_csrf = element["data-csrf"]
        url = (
            "https://web-1.gate2dark.online/index.php?members/find&_xfRequestUri=%2Fmembers%2F&_xfWithData=1&_xfResponseType=json&_xfToken="
            + data_csrf
            + "&q="
            + user
        )
        response = requests.post(url, cookies=cookies)
        json_data = response.json()
        for item in json_data["results"]:
            id_value = item["id"]
            if id_value.lower() == user.lower():
                userID = item["iconHtml"].split('data-user-id="')[1].split('"')[0]
                userStatus(True, f"{name}(userID: {userID})")
    except Exception as e:
        notSearch(name)


def bdfClub(user):
    url = "https://bdfclub.com"
    name = "BDF CLUB"
    try:
        response = requests.get(url)
        cookies = response.cookies
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        element = soup.find(id="XF")
        data_csrf = element["data-csrf"]
        url = (
            "https://bdfclub.com/index.php?members/find&_xfRequestUri=%2Fmembers%2F&_xfWithData=1&_xfResponseType=json&_xfToken="
            + data_csrf
            + "&q="
            + user
        )
        response = requests.post(url, cookies=cookies)
        json_data = response.json()
        for item in json_data["results"]:
            id_value = item["id"]
            if id_value.lower() == user.lower():
                userStatus(True, name)
    except Exception as e:
        notSearch(name)


def infectedZone(user):
    url = "https://infected-zone.com"
    name = "infected-zone"
    try:
        response = requests.get(url)
        cookies = response.cookies
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        element = soup.find(id="XF")
        data_csrf = element["data-csrf"]
        url = (
            "https://infected-zone.com/index.php?members/find&&_xfRequestUri=%2Fforum%2F&_xfWithData=1&_xfToken="
            + data_csrf
            + "&_xfResponseType=json&q="
            + user
        )
        response = requests.get(url, cookies=cookies)
        json_data = response.json()
        for item in json_data.get("results", []):
            id_value = item.get("id", "").lower()
            text = item.get("text")
            icon_html = item.get("iconHtml", "")

            if id_value == user.lower():
                # Process 'iconHtml' directly within the main loop
                avatar_span = BeautifulSoup(icon_html, "html.parser").find(
                    "span", class_="avatar--xxs"
                )
                data_user_id = avatar_span.get("data-user-id")
                userStatus(True, name + f"(userID: {data_user_id})")
                return
    except Exception as e:
        notSearch(name)


def Wjunction(user):
    url = "https://www.wjunction.com/"
    name = "Wjunction"
    try:
        response = requests.get(url)
        cookies = response.cookies
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        element = soup.find(id="XF")
        data_csrf = element["data-csrf"]
        url = (
            "https://www.wjunction.com/index.php?members/find&_xfRequestUri=%2Fmembers%2F&_xfWithData=1&_xfResponseType=json&_xfToken="
            + data_csrf
            + "&q="
            + user
        )
        response = requests.post(url, cookies=cookies)
        json_data = response.json()
        for item in json_data["results"]:
            id_value = item["id"]
            if id_value.lower() == user.lower():
                userStatus(True, name)
    except Exception as e:
        notSearch(name)


def landzdown(user):
    url = "https://www.landzdown.com/index.php?action=mlist;sa=search"
    name = "landzdown"
    payload = {"search": user, "fields[]": "name", "submit": "Search"}

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find_all("td", class_="real_name lefttext")

        found = any(row.get_text(strip=True) == user for row in rows)

        if found:
            user_link = soup.find("a", title=f"View the profile of {user}")

            if user_link:
                user_url = user_link["href"]
                user_id = user_url.split("=")[-1]
                userStatus(True, name + f"(userID: {user_id})")

    except Exception as e:
        print(e)
        notSearch(name)


def bhcforums(user):
    url = "https://bhcforums.cc/xmlhttp.php"
    name = "bhcforums.cc"
    query_params = {
        "action": "get_users",
        "query": user,
    }
    local_headers = headers.copy()

    del local_headers["Accept-Encoding"]

    query_string = urlencode(query_params)
    full_url = f"{url}?{query_string}"

    response = requests.get(full_url, headers=local_headers)
    try:
        json_data = response.json()
        found = any(
            "id" in user_info and user_info["id"] == f"{user}"
            for user_info in json_data
        )

        if found:
            userStatus(True, name)
    except:
        notSearch(name)


def enclavecc(user):
    query_params = {
        "q": user,
        "type": "core_members",
        "joinedDate": "any",
        "group[4]": "1",
        "group[19]": "1",
        "group[9]": "1",
        "group[12]": "1",
        "group[22]": "1",
        "group[6]": "1",
        "group[3]": "1",
        "group[7]": "1",
        "group[18]": "1",
        "group[23]": "1",
        "group[20]": "1",
        "group[21]": "1",
        "group[14]": "1",
        "group[15]": "1",
        "group[16]": "1",
        "group[10]": "1",
    }
    url = "https://www.enclave.cc/index.php"
    name = "enclave.cc"
    query_string = urlencode(query_params)
    userUrl = f"{url}?/search/&{query_string}"

    try:
        response = requests.get(userUrl, headers=headers)
        if (
            "There were no results for your search. Try broadening your criteria or choosing a different content area."
            in response.text
        ):
            pass
        elif response.status_code == 200:
            if (f"Go to {user}'s profile") in response.text:
                soup = BeautifulSoup(response.text, "html.parser")
                a_tags = soup.find_all("a", href=True)

                for a_tag in a_tags:
                    href_value = a_tag["href"]
                    match = re.search(r"/profile/(\d+)-\w+/", href_value)
                    if match:
                        userid = match.group(1)
                        break
                userStatus(True, name + f"(userID: {userid})")
    except:
        notSearch(name)
    time.sleep(2)


def nullbb(user):
    url = "https://nulledbb.com/xmlhttp.php"
    name = "NulledBB"
    query_params = {
        "action": "get_users",
        "query": user,
    }
    local_headers = headers.copy()

    del local_headers["Accept-Encoding"]

    query_string = urlencode(query_params)
    full_url = f"{url}?{query_string}"

    response = requests.get(full_url, headers=local_headers)
    try:
        json_data = response.json()
        found = any(
            "id" in user_info and user_info["id"] == f"{user}"
            for user_info in json_data
        )

        if found:
            user_id = json_data[0]["uid"]
            userStatus(True, name + f"(userID: {user_id})")
    except:
        notSearch(name)


def wilderssecurity(user):
    url = "https://www.wilderssecurity.com/search/search"
    name = "wilderssecurity"
    payload = {"keywords": "", "users": user, "date": "", "_xfToken": ""}
    try:
        response = requests.post(url, headers=headers, data=payload)
        if "The following members could not be found" not in response.text:
            userStatus(True, name)
    except:
        notSearch(name)


if __name__ == "__main__":
    while True:
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
        megatop(user)
        dark2web(user)
        bdfClub(user)
        infectedZone(user)
        Wjunction(user)
        bhcforums(user)
        enclavecc(user)
        nullbb(user)
        hostingforums(user)
        landzdown(user)
        wilderssecurity(user)
        breachForums(user)

        print(colored.green("\n>>> DETECTED: "))
        for i in forum:
            print("\t" + i)

        print(colored.red("\n>>> unknown: ", errorForum))
        for i in errorForum:
            print("\t" + i)

        print("\n")
        print(
            colored.white(
                "----------------------------------------------------------KILLER WHALE _whs"
            )
        )

        # clear list
        forum.clear()
        errorForum.clear()
