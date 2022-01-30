from bs4 import BeautifulSoup
import requests


SITE = "www.lego.com"


def check_stock(url):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return "Page not found"

    text = req.text
    # second term was added to avoid warning, as instructed by module terminal output
    soup = BeautifulSoup(text, features="lxml")
    matches = [item for item in soup.find_all(
    ) if "data-test" in item.attrs and item["data-test"] == "product-overview-availability"]

    return matches[0].get_text()


def get_product_name(url):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return "Page not found"

    text = req.text
    # second term was added to avoid warning, as instructed by module terminal output
    soup = BeautifulSoup(text, features="lxml")

    matches = [item for item in soup.find_all(
    ) if "data-test" in item.attrs and item["data-test"] == "product-overview-name"]

    return matches[0].get_text()
