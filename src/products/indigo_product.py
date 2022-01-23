from bs4 import BeautifulSoup
import requests

SITE = "www.chapters.indigo.ca"


def check_stock(url):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return "Page not found"

    text = req.text
    # second term was added to avoid warning, as instructed by module terminal output
    soup = BeautifulSoup(text, features="lxml")
    stock_status = soup.find(
        "span", class_="online-availability__availability-text")

    # the html layout of 'in stock' and 'out of stock' are slightly different so we have to look for different tags
    if stock_status:
        stock_status = stock_status.get_text()
    else:
        stock_status = soup.find(
            "div", class_="online-availability__shipping-message").get_text()

    return stock_status


def get_product_name(url):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return "Page not found"

    text = req.text
    # second term was added to avoid warning, as instructed by module terminal output
    soup = BeautifulSoup(text, features="lxml")

    return soup.find("h1", class_="product-title").get_text()
