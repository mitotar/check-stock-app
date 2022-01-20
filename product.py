from bs4 import BeautifulSoup
import requests

from web_helper import get_product_name, get_site_name


class Product:
    def __init__(self, url, nickname=None):
        req = requests.get(url)
        text = req.text
        # second term was added to avoid warning, as instructed by module terminal output
        soup = BeautifulSoup(text, features="lxml")

        self._url = url
        self._product_nickname = nickname
        self._site_name = get_site_name(url)  # indigo or lego
        self._product_name = get_product_name(
            url, self.site_name)  # unimplemented right now

    @property
    def url(self):
        return self._url

    @property
    def product_nickname(self):
        return self._product_nickname

    @property
    def site_name(self):
        return self._site_name

    @property
    def product_name(self):
        return self._product_name

    @classmethod
    def check_stock(cls, product):
        """
        Method needs to be static to use in html file.
        """

        try:
            req = requests.get(product.url)
        except requests.exceptions.ConnectionError:
            return "Page not found"

        text = req.text
        # second term was added to avoid warning, as instructed by module terminal output
        soup = BeautifulSoup(text, features="lxml")

        if product.site_name == "www.chapters.indigo.ca":
            stock_status = soup.find(
                "span", class_="online-availability__availability-text")

            # the html layout of 'in stock' and 'out of stock' are slightly different so we have to look for different tags
            if stock_status:
                stock_status = stock_status.get_text()
            else:
                stock_status = soup.find(
                    "div", class_="online-availability__shipping-message").get_text()

        elif product.site_name == "www.lego.com":
            matches = [item for item in soup.find_all(
            ) if "data-test" in item.attrs and item["data-test"] == "product-overview-availability"]
            stock_status = matches[0].get_text()

        return stock_status
