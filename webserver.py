from http.server import BaseHTTPRequestHandler, HTTPServer
import scraper
from bs4 import BeautifulSoup


class SimpleHTTPServerRequestHandler(BaseHTTPRequestHandler):

    #Get
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Run web scraper
        test_url = 'https://realpython.com/blog/'
        raw_html = scraper.get_raw_html(test_url)
        html = BeautifulSoup(raw_html, 'html.parser')
        message = str(scraper.pull_text(html))

        # self.wfile.write(bytes(message, "utf8"))
        html_message = str(html)
        self.wfile.write(bytes(html_message, "utf8"))
        return


def run():
    print('Starting server...')

    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, SimpleHTTPServerRequestHandler)

    print('Running server...')

    httpd.serve_forever()


if __name__ == '__main__':
    run()
