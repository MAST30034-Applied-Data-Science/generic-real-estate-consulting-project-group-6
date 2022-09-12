import pandas as pd


opt_dir = "../data/raw"

vic_income = pd.read_excel(f"{opt_dir}/external_data/income_SA2.xls", sheet_name="Table 1.4", skiprows=lambda x : x not in [6] + list(range(586, 1048)))
vic_income.to_csv(f"{opt_dir}/external_data/income_SA2_vic.csv")


sheet_names = ["Vic.", "Greater Melbourne", "Rest of Vic."]
path_names = ["vic", "greater_melbourne", "rest_vic"]
for i in range(0, 3):
    popu_pred = pd.read_excel(f"{opt_dir}/external_data/population_pred.xls", sheet_name=sheet_names[i], skiprows=lambda x : x not in [5] + list(range(41, 50)) + list(range(52,56)))
    popu_pred = popu_pred.rename(columns={"Unnamed: 0" : "stat", "Unnamed: 1" : "unit"})
    popu_pred = popu_pred.set_index("stat")
    popu_pred = popu_pred.drop(["unit","2017(a)"], axis=1)
    popu_pred = popu_pred.transpose()

    # popu_pred.to_csv(f"{opt_dir}/external_data/population_pred_{sheet_names[i]}.csv")
    popu_pred.to_csv(f"{opt_dir}/external_data/population_pred_{path_names[i]}.csv")

sa_popu = pd.read_excel(f"{opt_dir}/external_data/population.xlsx", sheet_name="Table 2", skiprows=lambda x : x not in [7] + list(range(9, 471)))
sa_popu = sa_popu.rename(columns={'no.': "ERP 2020", 'no..1' : "ERP 2021", 
                        'no..2':"ERP Change Amount", '%':"ERP Change Rate", 
                        'no..3':"Natureal increase", 'no..4':"Internal migration", 
                        'no..5': "Overseas migration", 'km2':"Area km2", 
                        'persons/km2' : "density 2021 persons/km2"})
sa_popu = sa_popu.drop(['Unnamed: 12', 'Unnamed: 15', 'Unnamed: 19'],  axis=1)
sa_popu.to_csv(f"{opt_dir}/external_data/population.csv")

income_new = pd.read_excel(f"{opt_dir}/external_data/income_SA2_2019.xlsx", sheet_name="Table 1.4", skiprows=lambda x : x not in [6] + list(range(586, 1048)))
selected_columns = ['2018-19', '2018-19.1', '2018-19.2','2018-19.3','2018-19.4']
income_pd = pd.read_csv(f"{opt_dir}/external_data/income_SA2_vic.csv")
income_pd = income_pd.drop(columns="Unnamed: 0")
for i in range(0, len(selected_columns)):
    income_pd.insert(loc=9 + 8 * i, column=selected_columns[i], value=income_new[selected_columns[i]])
income_pd.to_csv(f"{opt_dir}/external_data/income_SA2_full.csv")