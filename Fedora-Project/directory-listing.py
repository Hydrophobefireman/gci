from bs4 import BeautifulSoup as bs
import requests as r
from urllib.parse import urljoin


def get_soup(url):
    page = r.get(url)
    soup = bs(page.text, "html.parser")
    return soup


def get_links(soup: bs) -> list:
    ret = []
    tr = soup.find_all("tr")[1:]  # dont include name/last modified/description etc
    for i in tr:
        ret.extend(i.find_all("a"))
    return ret


def absolute_url(relative, base):
    return urljoin(base, relative)


def scrape(url=None):
    if url is None:
        url = input("enter URL:")
    soup = get_soup(url)
    links = get_links(soup)
    if len(links):
        print("Links Found:")
        for i, link in enumerate(links):
            href = absolute_url(link.attrs.get("href"), url)
            print(f"{i}. {href}")
    else:
        print("No Links found, check the page again")


if __name__ == "__main__":
    import sys

    arg = None
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    scrape(arg)
