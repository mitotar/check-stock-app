from bs4 import BeautifulSoup
import requests

SITE = "www.boardgamebliss.com"


def check_stock(url):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return "Page not found"

    text = req.text
    # second term was added to avoid warning, as instructed by module terminal output
    soup = BeautifulSoup(text, features="lxml")
    return soup.find(
        "span", class_="product-form__inventory").get_text()


def get_product_name(url):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return "Page not found"

    text = req.text
    # second term was added to avoid warning, as instructed by module terminal output
    soup = BeautifulSoup(text, features="lxml")

    return soup.find("h1", class_="product-meta__title").get_text()
