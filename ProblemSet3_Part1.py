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

# %% Task 4.1

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)


# %% Task 4.2

#Split the headerLineString into a list of header items based on commas
headerItems = headerLineString.split(',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index("mmsi")
name_idx = headerItems.index("shipname")
fleet_idx = headerItems.index("fleet_name")

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3
#Create an empty dictionary
vesselDict = {}
#Iterate through all lines (except the header) in the data file:
for item in lineList[1:]: #read from second line(exclude header)
    #Split the data into values
    values = item.split(',')
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = values[mmsi_idx]
    #Extract the fleet value
    fleet = values[fleet_idx]
    #Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet






# %% Task 4.4
vesselID = "440196000"
print("Vessel #" + vesselID + " flies the flag of " + vesselDict["440196000"])

# %%
