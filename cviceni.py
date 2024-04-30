import pickle
import os

class Address:
    def __init__(self, city, street, apartment):
        self.city = city
        self.street = street
        self.apartment = apartment

    def __str__(self):
        return f'City: {self.city}, Street: {self.street}, Apartment: {self.apartment}'

def create_path(file_name):
    # Get the directory of the script being run
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Join the script directory and the file name to create a full file path
    return os.path.join(script_dir, file_name)

def serialize(file_name, data):
    # Create a full file path
    path = create_path(file_name)
    # Open the file in write mode
    with open(path,"wb") as file:
        # Serialize and save data to the file
        pickle.dump(data, file)

# Define a function to load data from a file and deserialize it
def deserialize(file_name):
    # Create a full file path
    path = create_path(file_name)
    # Open the file in read mode
    with open(path, "rb") as file:
        # Load and deserialize data from the file
        data = pickle.load(file)
    # Return the deserialized data
    return data
