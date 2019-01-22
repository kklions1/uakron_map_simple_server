from bs4 import BeautifulSoup
import scraper


def main():
    test_url = 'https://realpython.com/blog/'
    raw_html = scraper.get_raw_html(test_url)
    html = BeautifulSoup(raw_html, 'html.parser')
    return scraper.pull_text(html)


if __name__ == "__main__":
    main()
