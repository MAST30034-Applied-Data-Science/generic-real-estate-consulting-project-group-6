## This file downloads all external dataset used in the project
# 1. austrialia post code datset
# 2. SA2 shape file
# 3. Population estimation by SA2
# 4. Income by SA2 12-19
# 5. Population prediction by states
# 6. Income by SA2 2020

import shutil
from urllib.request import urlretrieve
import os
import urllib.request
from zipfile import ZipFile

print('Set up dir')
# directory to store data
output_relative_dir = '../data/raw/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)

if not os.path.exists(output_relative_dir + 'external_data'):
    os.makedirs(output_relative_dir + "external_data")

if os.path.exists(output_relative_dir + 'external_data/SA2_shape'):
    shutil.rmtree(output_relative_dir + 'external_data/SA2_shape', ignore_errors=False, onerror=None)
os.makedirs(output_relative_dir + "external_data/SA2_shape")

if os.path.exists(output_relative_dir + 'external_data/SA2_shape_2016'):
    shutil.rmtree(output_relative_dir + 'external_data/SA2_shape_2016', ignore_errors=False, onerror=None)
os.makedirs(output_relative_dir + "external_data/SA2_shape_2016")

if os.path.exists(output_relative_dir + 'external_data/vic_localities'):
    shutil.rmtree(output_relative_dir + 'external_data/vic_localities', ignore_errors=False, onerror=None)
os.makedirs(output_relative_dir + "external_data/vic_localities")




print('Start Downloading .......')
# Add header to the request, so the website do not block request.
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
urllib.request.install_opener(opener)


# Download postcode data from https://www.matthewproctor.com/Content/postcodes/australian_postcodes.csv
postcode_output_dir =f"{output_relative_dir}/external_data/australian_postcodes.csv"
urllib.request.urlretrieve("https://www.matthewproctor.com/Content/postcodes/australian_postcodes.csv", postcode_output_dir)
print("australian_postcodes.csv finished")

# Download SA2 2020 Data from 
# https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3
# /jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip
SA_shape_zip_dir = f"{output_relative_dir}/external_data/SA2_shape/SA2_2021_AUST_SHP_GDA2020.zip"
urllib.request.urlretrieve("https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip", SA_shape_zip_dir)
print("SA2_2021_AUST_SHP_GDA2020.zip finished")
print("Start unzip SA2_2021_AUST_SHP_GDA2020.zip")
# Unzip SA2_2021_AUST_SHP_GDA2020.zip
SA_UNZIP_DIR = f"{output_relative_dir}/external_data/SA2_shape"
with ZipFile(SA_shape_zip_dir, 'r') as zipObj:
    zipObj.extractall(SA_UNZIP_DIR)
print("Unzip SA2_2021_AUST_SHP_GDA2020.zip finished")


# Download SA2 2016 Data from 
# https://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055001_sa2_2016_aust_shape.zip&1270.0.55.001&Data Cubes&A09309ACB3FA50B8CA257FED0013D420&0&July 2016&12.07.2016&Latest
SA_shape_2016_zip_dir = f"{output_relative_dir}/external_data/SA2_shape_2016/SA2_2016.zip"
urllib.request.urlretrieve("https://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055001_sa2_2016_aust_shape.zip&1270.0.55.001&Data%20Cubes&A09309ACB3FA50B8CA257FED0013D420&0&July%202016&12.07.2016&Latest", SA_shape_2016_zip_dir)
print("SA2_2016.zip finished")
print("Start unzip SA2_2016.zip")
# Unzip SA2_2021_AUST_SHP_GDA2020.zip
SA_2016_UNZIP_DIR = f"{output_relative_dir}/external_data/SA2_shape_2016"
with ZipFile(SA_shape_2016_zip_dir, 'r') as zipObj:
    zipObj.extractall(SA_2016_UNZIP_DIR)
print("Unzip SA2_2016.zip finished")


# Download victoria locality Data from 
# https://data.gov.au/data/dataset/af33dd8c-0534-4e18-9245-fc64440f742e/resource/4494abe0-64ea-4fa6-931a-d1a389a14e57/download/vic_localities.zip
Suburb_shape_dir = f"{output_relative_dir}/external_data/vic_localities/vic_localities.zip"
urllib.request.urlretrieve("https://data.gov.au/data/dataset/af33dd8c-0534-4e18-9245-fc64440f742e/resource/4494abe0-64ea-4fa6-931a-d1a389a14e57/download/vic_localities.zip", Suburb_shape_dir)
print("vic_localities.zip finished")
print("Start unzip vic_localities.zip")
# Unzip SA2_2021_AUST_SHP_GDA2020.zip
Suburb_shape_UNZIP_DIR = f"{output_relative_dir}/external_data/vic_localities"
with ZipFile(Suburb_shape_dir, 'r') as zipObj:
    zipObj.extractall(Suburb_shape_UNZIP_DIR)
print("Unzip vic_localities.zip finished")


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

# Download latest income from
# https://www.abs.gov.au/statistics/labour/earnings-and-working-conditions/personal-income-australia/2014-15-2018-19/6524055002_DO001.xlsx
income_2020_dir = f"{output_relative_dir}/external_data/income_SA2_2019.xlsx"
urllib.request.urlretrieve("https://www.abs.gov.au/statistics/labour/earnings-and-working-conditions/personal-income-australia/2014-15-2018-19/6524055002_DO001.xlsx", income_2020_dir)
print("income_SA2_2019.xlsx finished")

# Download LGA recorded offence from
# https://files.crimestatistics.vic.gov.au/2022-09/Data_Tables_LGA_Recorded_Offences_Year_Ending_June_2022.xlsx
offence_dir = f"{output_relative_dir}/external_data/recorded_offences.xlsx"
urllib.request.urlretrieve('https://files.crimestatistics.vic.gov.au/2022-09/Data_Tables_LGA_Recorded_Offences_Year_Ending_June_2022.xlsx', offence_dir)
print("recorded_offences.xlsx finished")

# Download School locations from
# https://www.education.vic.gov.au/Documents/about/research/datavic/dv309_schoollocations2021.csv
school_dir = f"{output_relative_dir}/external_data/school_location.csv"
urllib.request.urlretrieve('https://www.education.vic.gov.au/Documents/about/research/datavic/dv309_schoollocations2021.csv',school_dir)
print("school_location.csv finished")

print("All dataset downloaded!!!")
