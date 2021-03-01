import requests


def work():
    user_url = input('Input the URL:\n')
    r = requests.get(user_url)
    if r.status_code == 200:
        with open('source.html', mode='wb') as fout:
            fout.write(r.content)
        return 'Content saved.'
    else:
        return f'The URL returned {r.status_code}!'


print(work())
