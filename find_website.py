from urllib.parse import urlparse

def find_site(url):
    domain = urlparse(url).hostname.split('.')[1]
    print(domain)
    return domain


if __name__ == "__main__":
    find_site('https://www.westernjournal.com/air-raid-sirens-wail-israel-hit-reportedly-iranian-made-rockets/')
