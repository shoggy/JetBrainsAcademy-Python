import requests


def work():
    user_url = input('Input the URL:\n')
    r = requests.get(user_url)
    if r.status_code == 200 and 'content' in r.json():
        return r.json()['content']
    else:
        return 'Invalid quote resource!'


print(work())
