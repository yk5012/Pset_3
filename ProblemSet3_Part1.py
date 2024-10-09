#%% Task 1 - Edit code to print as requested

mountain = "Denali"
nickname = "'Mt. McKinley'"
elevation = "20322" 

print (mountain + ", sometimes \ncalled " + nickname + ",")
print ("is " + elevation + "'" + 'above sea level.' )

#%% Task 2 - Lists and Iteration

data_folder = r"W:\859_data\triangle"
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]
user_item = "roads.shp"
data_list.append(user_item)

for item in data_list:
    print(data_folder + "\\" + item)

# %% Task 3 - 
