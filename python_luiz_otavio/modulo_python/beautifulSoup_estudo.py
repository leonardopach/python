import re

import requests
from bs4 import BeautifulSoup

url = "http://localhost:3000/"
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, "html.parser")

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

tops_jobs_heading = parsed_html.select_one("#intro > div > div > article > h2")
print(tops_jobs_heading)

if tops_jobs_heading is not None:
    article = tops_jobs_heading.parent
    if article is not None:
        # print(article.text)
        for p in article.select("p"):
            print(re.sub(r"\s{1,}", " ", p.text))
