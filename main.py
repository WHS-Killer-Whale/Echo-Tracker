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


