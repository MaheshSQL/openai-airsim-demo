import airsim
import os
import time

time.sleep(0)

dict_of_objects = {'origin': [0.0, 0.0, 0.0], 
                   'Building-A': [105, -0.78, -37.79]}


def get_client():
    # connect to the AirSim simulator
    client = airsim.MultirotorClient()
    client.confirmConnection()
    client.enableApiControl(True)
    client.armDisarm(True)
    return client

#This functions returns value as dictinary of x, y and z
#Example: {   'x_val': -0.150694340467453, 'y_val': 0.0959537923336029, 'z_val': -1.8574612140655518}
def get_Current_Location(client):
    return client.getMultirotorState().kinematics_estimated.position

def take_Off(client):
    client.takeoffAsync().join()

def go_Forward(client, distance):
    current_location = get_Current_Location(client)
    client.moveToPositionAsync(current_location.x_val+distance, current_location.y_val, current_location.z_val, 4).join()

def go_Back(client, distance):
    current_location = get_Current_Location(client)
    client.moveToPositionAsync(current_location.x_val-distance, current_location.y_val, current_location.z_val, 4).join()

def go_Right(client, distance):
    current_location = get_Current_Location(client)
    client.moveToPositionAsync(current_location.x_val, current_location.y_val+distance, current_location.z_val, 4).join()

def go_Left(client, distance):
    current_location = get_Current_Location(client)
    client.moveToPositionAsync(current_location.x_val, current_location.y_val-distance, current_location.z_val, 4).join()

def go_Up(client, distance):
    current_location = get_Current_Location(client)
    client.moveToPositionAsync(current_location.x_val, current_location.y_val, current_location.z_val-distance, 4).join()

def go_Down(client, distance):
    current_location = get_Current_Location(client)
    client.moveToPositionAsync(current_location.x_val, current_location.y_val, current_location.z_val+distance, 4).join()