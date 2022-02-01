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


def check_price(url):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return "Page not found"

    text = req.text
    # second term was added to avoid warning, as instructed by module terminal output
    soup = BeautifulSoup(text, features="lxml")

    price = soup.find("span", attrs={"data-test": "product-price-sale"})
    if price:  # sale price
        price = price.get_text().replace("Sale Price", "$")
    else:
        price = soup.find("span", attrs={"data-test": "product-price"})
        if price:  # regular price
            price = price.get_text().replace("Price", "$")
        else:  # no price (retired product)
            price = "--------------"

    return price


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
