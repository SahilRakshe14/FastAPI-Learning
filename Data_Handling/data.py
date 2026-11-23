# Import required module.
import json


# Load student data from JSON file.
def load_data():
    with open("student.json", "r") as file:
        return json.load(file)