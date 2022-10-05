"""
Scrape property URL list form the Domain Pagination Component.
Store the property URL list in property_url.csv

"""

import pandas as pd
import re
from json import dump

from collections import defaultdict

# user packages
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

post_codes = pd.read_csv("../data/raw/external_data/australian_postcodes.csv")
post_codes = post_codes.loc[post_codes["state"] == "VIC"]
post_codes = post_codes["postcode"]
post_codes = post_codes.drop_duplicates()

BASE_URL = "https://www.domain.com.au"
PAGE_SIZE = 20
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"
}

# begin code
url_links = []

for post_code in post_codes:
    url = BASE_URL + f"/rent/?postcode={post_code}&page=1"
    bs_object = BeautifulSoup(requests.get(
    url, headers=headers).text, "html.parser")

    print(f"\n\npost_code {post_code}")
    if not bs_object:
        print(f"post_code {post_code} is not found")
        continue

    summary = bs_object.find("h1", {"data-testid": "summary"}).findAll("strong")

    num_prop = int(re.findall(r'\d+\s', summary[0].text)[0])

    max_pages = int(num_prop / PAGE_SIZE) + (num_prop % PAGE_SIZE > 0)
    print(f"    {max_pages} pages")
    
    n_pages = range(1, max_pages + 1)
    
    if max_pages != 0:
        print("    Start Scraping")
        for page in n_pages:
            url = BASE_URL + f"/rent/?postcode={post_code}&page={page}"

            bs_object = BeautifulSoup(requests.get(
            url, headers=headers).text, "html.parser")

            # find the unordered list (ul) elements which are the results, then
            # find all href (a) tags that are from the base_url website.            
            index_links = bs_object \
                .find(
                    "ul",
                    {"data-testid": "results"}
                ) \
                .findAll(
                    "a",
                    href=re.compile(f"{BASE_URL}/*") # the `*` denotes wildcard any
                )
            
            # print(f"\nThis is the index link: {index_links}\n")

            for link in index_links:
                # if its a property address, add it to the list
                if 'address' in link['class']:
                    url_links.append(link['href'])
                    # print(f"            add link {link['href']}")
        print(f"      Postcode : {post_code} Finishes, currently have {len(url_links)} links for property") 

url_series = pd.Series(url_links)
url_series = url_series.drop_duplicates()
url_series.to_csv("../data/raw/property_url.csv")