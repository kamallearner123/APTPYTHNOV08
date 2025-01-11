import json

# Create a dictionary with string keys and list values
data = {
    "fruits": ["apple", "banana", "cherry"],
    "vegetables": ["carrot", "broccoli", "spinach"],
    "grains": ["rice", "wheat", "quinoa"]
}

# Save the dictionary as a JSON file
json_file = 'data.json'
try:
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)  # Write JSON with indentation for readability
    print(f"Dictionary has been saved to {json_file}.")

    # Read the JSON file back into a dictionary
    with open(json_file, 'r') as file:
        loaded_data = json.load(file)
    print("Dictionary read from JSON file:")
    print(loaded_data)
except Exception as e:
    print(f"An error occurred: {e}")
