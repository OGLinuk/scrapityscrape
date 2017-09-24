'''
Scrapity Scrape
https://github.com/OGLinuk/scrapityscrape
'''
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

def main():

    # BeautifulSoup implementation
    print('Please enter a url')
    url = input()
    sauce = uReq(url)
    page_html = sauce.read()
    sauce.close()
    soup = bs(page_html, "html.parser")

    # HTML parsing
    containers = soup.find('body')
    print(containers)

    # Writing to file - payload.txt
    with open('payload.txt', 'ab+') as f:
        f.write(bytes('\n{0}\n\n'.format(container_payload), 'UTF-8'))
    f.close()

if __name__ == '__main__':
    main()
