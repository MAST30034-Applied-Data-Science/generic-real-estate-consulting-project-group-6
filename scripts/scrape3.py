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
    # bs_object = BeautifulSoup(urlopen(property_url), "lxml")
    print(f"\n    Scraping {property_url}")
    bs_object = BeautifulSoup(requests.get(
    property_url, headers=headers).text, "html.parser")

    i += 1
    print(f"    The {i}th property")

    # looks for the header class to get property name
    prop_name_bs = bs_object.find("h1", {"class": "css-164r41r"})
    if not prop_name_bs:
        print("skip name")
        continue
    property_metadata[property_url]['name'] = prop_name_bs.text
    # print(f"    property name : {prop_name_bs.text}")

    # looks for the div containing a summary title for cost
    prop_cost_bs = bs_object.find("div", {"data-testid": "listing-details__summary-title"})
    if not prop_cost_bs:
        print("skip cost")
        continue
    property_metadata[property_url]['cost_text'] = prop_cost_bs.text
    # print(f"    property cost : {prop_cost_bs.text}")

    # extract coordinates from the hyperlink provided
    # i'll let you figure out what this does :P
    prop_posi_bs = bs_object.find(
                    "a",
                    {"target": "_blank", 'rel': "noopener noreferer"}
                  )
    if not prop_posi_bs:
        print("skip position")
        continue
    property_metadata[property_url]['coordinates'] = [
        float(coord) for coord in re.findall(
            r'destination=([-\s,\d\.]+)', # use regex101.com here if you need to
            prop_posi_bs.attrs['href']
        )[0].split(',')
    ]
    
    #find rooms of the property
    property_metadata[property_url]['rooms'] = []
    rooms = []
    prop_feature_bs = bs_object.find("div", {"data-testid": "property-features"})
    if not prop_feature_bs:
        print("skip feature")
        continue
    prop_rooms_bs = prop_feature_bs.findAll("span", {"data-testid": "property-features-text-container"})
    if not prop_rooms_bs:
        print("skip rooms")
        continue
    for feature in prop_rooms_bs:
        regexopt = re.findall(r'\d\s[A-Za-z]+', feature.text)
        if len(regexopt) != 0:
            property_metadata[property_url]['rooms'].append(regexopt[0])
            rooms.append(regexopt[0])
    # print(f"    Property rooms : {rooms}")

    #find property description
    # property_metadata[property_url]['desc'] = re \
    #     .sub(r'<br>', '\n', str(bs_object.find("p"))) \
    #     .strip('</p>')
    # print(property_metadata[property_url]['desc'])

    #find property type Apartment? House?
    prop_type_container_bs = bs_object.find("div", {"data-testid": "listing-summary-property-type"})
    if not prop_type_container_bs:
        print("skip type container")
        continue
    prop_type_bs = prop_type_container_bs.find("span")
    if not prop_type_bs:
        print("skip type")
        continue
    property_metadata[property_url]['type'] = prop_type_bs.text
    # print(f"    Property type : {prop_type_bs.text}")



print("Stage Two Finishes")

# output to example json in data/raw/
with open('../data/raw/example.json', 'w') as f:
    dump(property_metadata, f)