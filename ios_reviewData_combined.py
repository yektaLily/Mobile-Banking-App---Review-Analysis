import pandas as pd 
import numpy as np 

bmo_raw_data = pd.read_csv("reviews_ios_bmo.csv")
cibc_raw_data = pd.read_csv("reviews_ios_cibc.csv")
rbc_raw_data = pd.read_csv("reviews_ios_rbc.csv")
scotia_raw_data = pd.read_csv("reviews_ios_scotia.csv")
td_raw_data = pd.read_csv("reviews_ios_td.csv")

# print(bmo_raw_data.head())
# print(bmo_raw_data.columns)

#columns are: isEdited, developerResponse, rating, title, date, userName, review 
#drop the unnecessary columns 
bmo_raw_data = bmo_raw_data.drop(columns = ['isEdited', 'developerResponse', 'userName']) 
cibc_raw_data = cibc_raw_data.drop(columns = ['isEdited', 'developerResponse', 'userName']) 
rbc_raw_data = rbc_raw_data.drop(columns = ['isEdited', 'developerResponse', 'userName']) 
scotia_raw_data = scotia_raw_data.drop(columns = ['isEdited', 'developerResponse', 'userName']) 
td_raw_data = td_raw_data.drop(columns = ['isEdited', 'developerResponse', 'userName']) 

# Version 1 of the data will not have dates either (but I'm keeping one version with dates for if we wanna do version based analysis)

v1_bmo_raw_df = bmo_raw_data.drop(columns=['date'])
v1_cibc_raw_data = cibc_raw_data.drop(columns=['date'])
v1_rbc_raw_data = rbc_raw_data.drop(columns=['date'])
v1_scotia_raw_data = scotia_raw_data.drop(columns=['date'])
v1_td_raw_data = td_raw_data.drop(columns=['date'])

# combining all of these together 
allbankinfos = {
    'BMO': v1_bmo_raw_df,
    'CIBC': v1_cibc_raw_data,
    'RBC': v1_rbc_raw_data, 
    'SCOTIA': v1_scotia_raw_data, 
    'TD': v1_td_raw_data

}

merged_df = pd.concat([df.assign(Bank = name) for name, df in allbankinfos.items()], ignore_index=True)

# print(merged_df.head())
# print(merged_df.info())

merged_df.to_csv("top5banksReviews_v1.csv")