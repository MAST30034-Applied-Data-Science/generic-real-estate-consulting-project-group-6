## Download the data
from urllib.request import urlretrieve
import os
import urllib.request


# directory to store data
output_relative_dir = '../data/raw/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
if not os.path.exists(output_relative_dir + 'external_data'):
    os.makedirs(output_relative_dir + "external_data")


# Add header to the request, so the website do not block request.
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
urllib.request.install_opener(opener)


# Download postcode data from https://www.matthewproctor.com/Content/postcodes/australian_postcodes.csv
postcode_output_dir =f"{output_relative_dir}/external_data/australian_postcodes.csv"
urllib.request.urlretrieve("https://www.matthewproctor.com/Content/postcodes/australian_postcodes.csv", postcode_output_dir)
print("australian_postcodes.csv finished")



