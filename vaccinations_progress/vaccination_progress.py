import pandas as pd
import numpy as np
import os
import sys

##--
vaccination_path = "../../covid-19-data/public/data/vaccinations"
country_files = os.listdir(os.path.join(vaccination_path, 'country_data'))
country_df = pd.DataFrame()
for country in country_files:
    data_df = pd.read_csv(os.path.join(vaccination_path, 'country_data', country))
    country_df = country_df.append(data_df)   

##-
vaccinations_df = pd.read_csv(os.path.join(vaccination_path, 'vaccinations.csv'))    
locations_df = pd.read_csv(os.path.join(vaccination_path, 'locations.csv'))
##-
selected_features = ["location", "vaccines", "source_name", "source_website"]
##-
country_vaccination_df = vaccinations_df.merge(locations_df[selected_features], on = ["location"])
##-
output_selected_columns = ['country', 'iso_code', 'date', 'total_vaccinations',
'people_vaccinated', 'people_fully_vaccinated',
       'daily_vaccinations_raw', 'daily_vaccinations',
       'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
       'people_fully_vaccinated_per_hundred', 'daily_vaccinations_per_million',
       'vaccines', 'source_name', 'source_website']
country_vaccination_df.columns = output_selected_columns
country_vaccination_df.to_csv("country_vaccinations.csv", index=False)