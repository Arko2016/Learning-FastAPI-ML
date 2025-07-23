'''
This will be used to try out different methods on the input json file before including in the main file
'''
import json

def convert_to_lower(obj,column):
    for item in obj.values():
        item[column] = item[column].lower()

with open('patients.json','r') as f:
    data = json.load(f)
    #print(data.values())
    #filter_list = list(set(x['city'] for x in data.values()))
    #print(filter_list)
    #filtered_data = [x for x in data.values() if x['gender'] == 'male']
    #print(len(filtered_data))
    
    filter_value = 'Mumbai'
    filtered_data = [x for x in data.values() if x['city'].lower() == filter_value.lower()]
    print(filtered_data)
    
    