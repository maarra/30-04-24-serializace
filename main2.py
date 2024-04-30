import json

class FootballClub:
    # Initialize an instance of the class
    def __init__(self, name, city, country):
        # Define the name, city, and country attributes of the class instance
        self.name = name
        self.city = city
        self.country = country

    # Define a method that returns a formatted string with full club information
    def get_full_information(self):
        return f"{self.name}{self.city}{self.country}"

    def to_json(self):
        return json.dumps(self.__dict__)

obj = FootballClub('Dynamo', 'Kyiv', 'Ukraine')

print(obj.get_full_information())

serialized_obj = obj.to_json()

print(serialized_obj)