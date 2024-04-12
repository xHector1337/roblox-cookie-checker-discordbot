import requests

def usernamechecker(cookie):
    client = requests.session()
    client.cookies['.ROBLOSECURITY'] = cookie
    api="https://users.roblox.com/v1/users/authenticated"
    response = client.get(api)
    return response.json().get('name')
def idchecker(cookie):
    client = requests.session()
    client.cookies['.ROBLOSECURITY'] = cookie
    api="https://users.roblox.com/v1/users/authenticated"
    response = client.get(api)
    return response.json().get('id')

def emailchecker(cookie):
    client = requests.session()
    client.cookies['.ROBLOSECURITY'] = cookie
    api="https://accountsettings.roblox.com/v1/email"
    response = client.get(api)
    return response.json()

def phonechecker(cookie):
    client = requests.session()
    client.cookies['.ROBLOSECURITY'] = cookie
    api="https://accountinformation.roblox.com/v1/phone"
    response = client.get(api)
    return response.json()

def robuxchecker(cookie):
    client = requests.session()
    client.cookies['.ROBLOSECURITY'] = cookie
    api = "https://economy.roblox.com/v1/user/currency"
    response = client.get(api)
    return response.json().get('robux')

def premiumchecker(cookie,id):
    client = requests.session()
    client.cookies['.ROBLOSECURITY'] = cookie
    api = f"https://premiumfeatures.roblox.com/v1/users/{id}/validate-membership"
    response = client.get(api)
    return response.json()