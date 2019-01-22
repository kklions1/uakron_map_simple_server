# Scrapes data from website
from requests import get
from requests.exceptions import RequestException
from contextlib import closing


def get_raw_html(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error("Error during request to {0} : {1}".format(url, str(e)))
        return None


def is_good_response(response):
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(error):
    print(error)


def pull_text(html):
    other_content = html.find('h1', attrs={'class': 'mb-2 display-3'})
    return other_content
