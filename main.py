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