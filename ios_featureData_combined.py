import numpy as np
import pandas as pd 
import data_iosApps 
from data_iosApps import data_ios_appInfo

data_list = []

for app_info in data_ios_appInfo:
    for app_name, details in app_info.items():
        details['Bank'] = app_name
        data_list.append(details)

df = pd.DataFrame(data_list)

df.to_csv("IOS_app_information.csv")
print(df.head())