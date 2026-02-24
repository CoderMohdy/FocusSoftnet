import re
import requests
from bs4 import BeautifulSoup

def find_contacts(website_url):
    try:
        r = requests.get(website_url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")

        text = soup.get_text()

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )

        return list(set(emails))[:3]

    except:
        return []