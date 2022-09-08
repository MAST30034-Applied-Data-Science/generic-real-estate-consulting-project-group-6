


import pandas as pd

vic_income = pd.read_excel("../data/raw/external_data/income_SA2.xls", sheet_name="Table 1.4", skiprows=lambda x : x not in [6] + list(range(586, 1048)))
vic_income.to_csv("../data/raw/external_data/income_SA2_vic.csv")


sheet_names = ["Vic.", "Greater Melbourne", "Rest of Vic."]
path_names = ["vic", "greater_melbourne", "rest_vic"]
for i in range(0, 3):
    popu_pred = pd.read_excel("../data/raw/external_data/population_pred.xls", sheet_name=sheet_names[i], skiprows=lambda x : x not in [5] + list(range(41, 50)) + list(range(52,56)))
    popu_pred = popu_pred.rename(columns={"Unnamed: 0" : "stat", "Unnamed: 1" : "unit"})
    popu_pred = popu_pred.set_index("stat")
    popu_pred = popu_pred.drop(["unit","2017(a)"], axis=1)
    popu_pred = popu_pred.transpose()
    popu_pred.to_csv(f"../data/raw/external_data/population_pred_{path_names[i]}.csv")

sa_popu = pd.read_excel("../data/raw/external_data/population.xlsx", sheet_name="Table 2", skiprows=lambda x : x not in [7] + list(range(9, 471)))
sa_popu = sa_popu.rename(columns={'no.': "ERP 2020", 'no..1' : "ERP 2021", 
                        'no..2':"ERP Change Amount", '%':"ERP Change Rate", 
                        'no..3':"Natureal increase", 'no..4':"Internal migration", 
                        'no..5': "Overseas migration", 'km2':"Area km2", 
                        'persons/km2' : "density 2021 persons/km2"})
sa_popu = sa_popu.drop(['Unnamed: 12', 'Unnamed: 15', 'Unnamed: 19'],  axis=1)
sa_popu.to_csv("../data/raw/external_data/population.csv")
