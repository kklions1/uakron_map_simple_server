import getpass
import requests
from urllib.request import urlopen


my_akron_url = 'https://my.uakron.edu/portprod/signon.html'


def login():
    username = input("Username: ")
    password = getpass.getpass()

    login_data = {
        'username': username,
        'password': password
    }

    session = requests.session()

    auth = session.post(my_akron_url, data=login_data)
    print(auth.url)
    
    # urlopen('https://www.google.com')


if __name__ == '__main__':
    login()
