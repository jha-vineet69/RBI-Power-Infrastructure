import pandas as pd
from functools import reduce

df_requirement = pd.read_csv('State-wise Power Requirement.csv')

column_list = df_requirement.columns.tolist()[1:]

df_requirement_new = df_requirement.melt(id_vars=['State/Union Territory'], value_vars=column_list).rename(columns = {'variable':'Year', 'value':'Power_Requirement_Net_Crore_Units'})
# print(df_requirement_new)


df_available = pd.read_csv('State-wise Availability of Power.csv')

column_list2 = df_available.columns.tolist()[1:]

df_available_new = df_available.melt(id_vars=['State/Union Territory'], value_vars=column_list2).rename(columns = {'variable':'Year', 'value':'Availability_Of_Power_Net_Crore_Units'})
# print(df_available_new)


df_available_per_capita = pd.read_csv('State-wise Per Capita Availability of Power.csv')

column_list3 = df_available_per_capita.columns.tolist()[1:]

df_available_per_capita_new = df_available_per_capita.melt(id_vars=['State/Union Territory'], value_vars=column_list3).rename(columns = {'variable':'Year', 'value':'Availability_Of_Power_Per_Capita_kiloWatt-Hour'})
# print(df_available_per_capita_new)


df_installed = pd.read_csv('State-wise Installed Capacity of Power.csv')

column_list4 = df_installed.columns.tolist()[1:]

df_installed_new = df_installed.melt(id_vars=['State/Union Territory'], value_vars=column_list4).rename(columns = {'variable':'Year', 'value':'Installed_Power_Capacity_MegaWatt'})
# print(df_installed_new)


# df_distribution = pd.read_csv('State-wise Electricity Transmission & Distribution Losses.csv')
#
# column_list5 = df_distribution.columns.tolist()[1:]
#
# df_distribution_new = df_distribution.melt(id_vars=['State/Union Territory'], value_vars=column_list5).rename(columns = {'variable':'Year', 'value':'Transmission_&_Distribution_Losses_%'})


# pd.merge(df_requirement_new, df_available_new, how='inner', on=['State/Union Territory','Year']).to_csv('Test.csv')

dfs = [df_requirement_new, df_available_new, df_available_per_capita_new, df_installed_new]
result_2 = reduce(lambda df_left,df_right: pd.merge(df_left, df_right,on=['State/Union Territory', 'Year'],how='inner'),dfs)

result_2.sort_values(['Year','State/Union Territory'], ascending=True).to_csv('India_Statewise_Power_Infrastructure_Data_RBI.csv', index=False)