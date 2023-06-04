import modules  
  
# Get the drone client object  
client = modules.get_client()  
  
# Define the starting location and the location of Building-A  
dict_of_objects = {'drone_origin': [0.0, 0.0, 0.0], 'Building-A': [105, -0.78, -37.79]}  
  
# Take off  
modules.take_Off(client)  
  
# Get the current location of the drone  
current_location = modules.get_Current_Location(client)  
  
# Calculate the distance to move on the z-axis to reach an elevation of 40 units  
z_distance = 40 - current_location.z_val  
  
# Move the drone up to an elevation of 40 units  
modules.go_Up(client, z_distance)  
  
# Get the current location of the drone  
current_location = modules.get_Current_Location(client)  
  
# Calculate the distance to move on the x-axis to reach Building-A  
x_distance = abs(dict_of_objects['Building-A'][0] - current_location.x_val)  
  
# Calculate the distance to move on the y-axis to reach Building-A  
y_distance = abs(dict_of_objects['Building-A'][1] - current_location.y_val)  
  
# Move the drone to Building-A  
if current_location.x_val < dict_of_objects['Building-A'][0]:  
    modules.go_Forward(client, x_distance)  
elif current_location.x_val > dict_of_objects['Building-A'][0]:  
    modules.go_Back(client, x_distance)  
  
if current_location.y_val < dict_of_objects['Building-A'][1]:  
    modules.go_Right(client, y_distance)  
elif current_location.y_val > dict_of_objects['Building-A'][1]:  
    modules.go_Left(client, y_distance)  
