from ..web_helper import get_site_name
from . import product_indigo as indigo
from . import product_lego as lego
from . import product_boardgamebliss as bgb
from . import product_amazon as amazon


SUPPORTED_SITES = [indigo.SITE, lego.SITE, bgb.SITE, amazon.SITE]


def create_product(url):
    site = get_site_name(url)

    if site == indigo.SITE:
        name = indigo.get_product_name(url)
    elif site == lego.SITE:
        name = lego.get_product_name(url)
    elif site == bgb.SITE:
        name = bgb.get_product_name(url)
    elif site == amazon.SITE:
        name = amazon.get_product_name(url)

    return [site, name]


def check_stock(site, url):
    if site == indigo.SITE:
        return indigo.check_stock(url)
    elif site == lego.SITE:
        return lego.check_stock(url)
    elif site == bgb.SITE:
        return bgb.check_stock(url)
    elif site == amazon.SITE:
        return amazon.check_stock(url)


def check_price(site, url):
    if site == indigo.SITE:
        return indigo.check_price(url)
    elif site == lego.SITE:
        return lego.check_price(url)
    elif site == bgb.SITE:
        return bgb.check_price(url)
    elif site == amazon.SITE:
        return amazon.check_price(url)
