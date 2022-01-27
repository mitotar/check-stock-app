import requests
import re


def is_url_valid(url):
    try:
        requests.get(url)
    except requests.exceptions.ConnectionError:
        return False

    return True


def get_site_name(url):
    """
    Returns the portion of the website between www. and .com or .ca.
    """

    return re.search(r"www.+\.c(a|om)", url).group(0)


if __name__ == "__main__":
    pass
