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

# %% Task 3 - Lists and iteration

user_numbers = []
for number in range(3):
    user_input = int(input("Enter an integer: ")) #input is always string so need to convert to integer to sort based on value
    user_numbers.append(user_input)
user_numbers.sort()
print(user_numbers[-1]) #this will always print largest value instead while user_numbers[2] assumes list will always be 3

# %% Task 3 - Challenge

user_numbers = []
for number in range(3):
    user_input = int(input("Enter an integer: "))
    user_numbers.append(user_input)
user_numbers.sort(reverse = True)
print(user_numbers)

# %%
