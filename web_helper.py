#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re


def is_url_valid(url):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return False

    return True


def get_product_name(url, site):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return "Page not found"

    text = req.text
    # second term was added to avoid warning, as instructed by module terminal output
    soup = BeautifulSoup(text, features="lxml")

    if site == "www.chapters.indigo.ca":
        product_name = soup.find("h1", class_="product-title").get_text()

    elif site == "www.lego.com":
        matches = [item for item in soup.find_all(
        ) if "data-test" in item.attrs and item["data-test"] == "product-overview-name"]
        product_name = matches[0].get_text()

    return product_name


def get_site_name(url):
    """
    Returns the portion of the website between www. and .com or .ca.
    """

    return re.search(r"www.+\.c(a|om)", url).group(0)


if __name__ == "__main__":
    pass
