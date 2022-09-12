import sys
import pandas as pd
import re
from json import dump

from collections import defaultdict

# user packages
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

BASE_URL = "https://www.domain.com.au"
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

url_links_pd = pd.read_csv("../data/raw/property_url.csv")
url_links_series = url_links_pd["0"]
url_links = url_links_series.tolist()

# begin code
property_metadata = defaultdict(dict)
i = 0

# for each url, scrape some basic metadata
for property_url in url_links[1:]:

    i += 1

    # bs_object = BeautifulSoup(urlopen(property_url), "lxml")    
    print(f"\n    Scraping {property_url}")

    try:
        bs_object = BeautifulSoup(requests.get(
        property_url, headers=headers).text, "html.parser")
        print(f"    The {i}th property")

        # looks for the header class to get property name
        property_metadata[property_url]['name'] = bs_object.find("h1", {"class": "css-164r41r"}).text
        print(f"    property name : {property_metadata[property_url]['name']}")

        # looks for the div containing a summary title for cost
        property_metadata[property_url]['cost_text'] = bs_object.find("div", 
                                                      {"data-testid": 
                                                        "listing-details__summary-title"}).text
        print(f"    property cost : {property_metadata[property_url]['cost_text']}")

        # extract coordinates from the hyperlink provided
        # i'll let you figure out what this does :P
        property_metadata[property_url]['coordinates'] = [
            float(coord) for coord in re.findall(
                r'destination=([-\s,\d\.]+)', # use regex101.com here if you need to
                bs_object.find(
                        "a",
                        {"target": "_blank", 'rel': "noopener noreferer"}
                      ).attrs['href']
            )[0].split(',')
        ]
        
        #find rooms of the property
        property_metadata[property_url]['rooms'] = []
        for feature in bs_object.find("div", {"data-testid": "property-features"}) \
                      .findAll("span", {"data-testid": "property-features-text-container"}):
            regexopt = re.findall(r'\d\s[A-Za-z]+', feature.text)
            if len(regexopt) != 0:
                property_metadata[property_url]['rooms'].append(regexopt[0])
        print(f"    Property rooms : {property_metadata[property_url]['rooms']}")

        #find property description
        # property_metadata[property_url]['desc'] = re \
        #     .sub(r'<br>', '\n', str(bs_object.find("p"))) \
        #     .strip('</p>')
        # print(property_metadata[property_url]['desc'])

        #find property type Apartment? House?
        property_metadata[property_url]['type'] = bs_object.find("div", 
                                                  {"data-testid": 
                                                    "listing-summary-property-type"}) \
                                                      .find("span").text
        print(f"    Property type : {property_metadata[property_url]['type']}")
    except KeyboardInterrupt:
        sys.exit()
    except :
        print(property_url + '  Error, Skip')
        continue
    

print("Stage Two Finishes")

# output to example json in data/raw/
with open('../data/raw/property_raw.json', 'w') as f:
    dump(property_metadata, f)