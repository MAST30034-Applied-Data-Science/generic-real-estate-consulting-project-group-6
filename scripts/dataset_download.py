## This file downloads all external dataset used in the project
# 1. austrialia post code datset
# 2. SA2 shape file
# 3. Population estimation by SA2
# 4. Income by SA2
# 5. Population prediction by states

import shutil
from urllib.request import urlretrieve
import os
import urllib.request
from zipfile import ZipFile


# directory to store data
output_relative_dir = '/root/generic-real-estate-consulting-project-group-6/data/raw/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)

if not os.path.exists(output_relative_dir + 'external_data'):
    os.makedirs(output_relative_dir + "external_data")

if os.path.exists(output_relative_dir + 'external_data/SA2_shape'):
    shutil.rmtree(output_relative_dir + 'external_data/SA2_shape', ignore_errors=False, onerror=None)
os.makedirs(output_relative_dir + "external_data/SA2_shape")



# Add header to the request, so the website do not block request.
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
urllib.request.install_opener(opener)


# Download postcode data from https://www.matthewproctor.com/Content/postcodes/australian_postcodes.csv
postcode_output_dir =f"{output_relative_dir}/external_data/australian_postcodes.csv"
urllib.request.urlretrieve("https://www.matthewproctor.com/Content/postcodes/australian_postcodes.csv", postcode_output_dir)
print("australian_postcodes.csv finished")

# Download SA2 Data from 
# https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3
# /jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip
SA_shape_zip_dir = f"{output_relative_dir}/external_data/SA2_shape/SA2_2021_AUST_SHP_GDA2020.zip"
urllib.request.urlretrieve("https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip", SA_shape_zip_dir)
print("SA2_2021_AUST_SHP_GDA2020.zip finished")
# Unzip SA2_2021_AUST_SHP_GDA2020.zip
TAXI_ZONE_UNZIP_DIR = f"{output_relative_dir}/external_data/SA2_shape"
with ZipFile(SA_shape_zip_dir, 'r') as zipObj:
    zipObj.extractall(TAXI_ZONE_UNZIP_DIR)

# Download population data from
# https://www.abs.gov.au/statistics/people/population/regional-population/2020-21/32180DS0001_2020-21.xlsx
population_dir = f"{output_relative_dir}/external_data/population.xlsx"
urllib.request.urlretrieve("https://www.abs.gov.au/statistics/people/population/regional-population/2020-21/32180DS0001_2020-21.xlsx", population_dir)
print("population.xlsx finished")

# Download area income data from
# https://www.abs.gov.au/statistics/labour/earnings-and-working-conditions/personal-income-australia/2011-12-2017-18/6524055002_DO001.xls
income_dir = f"{output_relative_dir}/external_data/income_SA2.xls"
urllib.request.urlretrieve("https://www.abs.gov.au/statistics/labour/earnings-and-working-conditions/personal-income-australia/2011-12-2017-18/6524055002_DO001.xls", income_dir)
print("income_SA2.xls finished")

# Download population prediction data from
# https://www.abs.gov.au/statistics/people/population/population-projections-australia/2017-base-2066/32220ds01_2017-2066_summary_statistics.xls
population_pred_dir = f"{output_relative_dir}/external_data/population_pred.xls"
urllib.request.urlretrieve("https://www.abs.gov.au/statistics/people/population/population-projections-australia/2017-base-2066/32220ds01_2017-2066_summary_statistics.xls", population_pred_dir)
print("population_pred.xls finished")





