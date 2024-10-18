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

# %% Task 4.4 Using your dictionary
vesselID = "440196000"
print("Vessel #" + vesselID + " flies the flag of " + vesselDict["440196000"])



# %% Task 5.1 open file and store header line in string
#Create a Python file object, i.e., a link to the file's contents
loiteringFile = open(file='data/raw/loitering_events_20180723.csv', mode='r')

#Read the entire contents into a list object
loiteringLines = loiteringFile.readlines()

#Release the link to the file objects (now that we have all its contents)
loiteringFile.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "loiteringHeader"
loiteringHeader = loiteringLines[0]

#Print the contents of the loiteringHeader
print(loiteringHeader)

# %% Task 5.2 split header names and obtain index  

#Split the loiteringHeader into a list of header items based on commas
loiteringHeaderItems = loiteringHeader.split(',')

#List the index of relevant header items
transshipment_mmsi_idx = loiteringHeaderItems.index("transshipment_mmsi")
start_lat_idx = loiteringHeaderItems.index("starting_latitude")
start_long_idx = loiteringHeaderItems.index("starting_longitude")
end_lat_idx = loiteringHeaderItems.index("ending_latitude")
end_long_idx = loiteringHeaderItems.index("ending_longitude")

#Print the values
print(transshipment_mmsi_idx,start_lat_idx,start_long_idx,end_lat_idx,end_long_idx )


#%% Task 5.3 

# Create empty list 
loitering_booleans_list = []

# Iterate through all lines starting on the second line 
for loiteringItem in loiteringLines[1:]:
    #Split each line by comma
    loiteringData = loiteringItem.split(",")

    #Store variables using the previously derived index values so that 
    #even if the column orders change, the code will still work 
    transshipment_mmsi = loiteringData[transshipment_mmsi_idx]
    start_lat = float(loiteringData[start_lat_idx])
    start_long = float(loiteringData[start_long_idx])
    end_lat = float(loiteringData[end_lat_idx])
    end_long = float(loiteringData[end_long_idx])

    # Create boolean condition for equator crossing
    # lat_bool is true is ship starts below equator and ends above equator
    lat_bool = start_lat < 0 < end_lat

    # Create second boolean condition for longitude
    start_long_bool = 145 < start_long < 155

    # If both booleans are true, append to empty list
    if lat_bool & start_long_bool:
        loitering_booleans_list.append(transshipment_mmsi)




#%% Task 5: Check values and print if meet criteria 
for mmsi in loitering_booleans_list:
    # retrieving flag values associated with the key mmsi from vesslDict into new list vessel_info 
    vessel_info = vesselDict.get(mmsi)
    #performing initial if check to run for each iteration in vessel_info
    if vessel_info:
        print("Vessel # " + mmsi + " flies the flag of " + vesselDict[mmsi])
if not loitering_booleans_list:
    print("No vessels met criteria")

