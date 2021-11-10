"""
A generic program that reads, sniff and dumps the schema of two json file

"""
import os
import sys
import json
from collections import defaultdict

#input json filename
input_file_name = "data_1.json"
#input json file path
input_file_path = os.path.join(os.curdir, "data", input_file_name)
#second input json filename
input_file_name_2 = "data_2.json"
#aecond input json file path
input_file_path_2 = os.path.join(os.curdir, "data", input_file_name_2)
#output schema filename for data_1.json
output_file_name = "schema_1.json"
#output schema file path for data_1.json
output_file_path = os.path.join(os.curdir, "schema", output_file_name)
#output schema filename for data_2.json
output_file_name_2 = "schema_2.json"
#output schema file path for data_2.json
output_file_path_2 = os.path.join(os.curdir, "schema", output_file_name_2)

message = defaultdict()
schema_data = defaultdict()


def getSchema(value):
    ''' The function determines the json data type '''
    schema_template = {"type": "string",
                       "tag": "",
                       "description": "",
                       "required": False
                       }
    if type(value) is str:
        return schema_template
    elif type(value) is int:
        schema_template["type"] = "integer"
        return schema_template
    elif type(value) is list and len(value) > 0:
        if type(value[0]) is dict:
            schema_template["type"] = "array"
        elif type(value[0]) is str:
            schema_template["type"] = "enum"
        return schema_template


def addToSchema(key, value, schema):
    ''' A recursive function that takes the key,
        value and a python dictionary to store the result in,
        for the json file with values such as "key":{"key1":"value"}
'''
    schema[key] = {}
    if type(value) is dict:
        for k, v in value.items():
            addToSchema(k, v, schema[key])
    else:
        schema[key] = getSchema(value)


if __name__ == "__main__":
    
    with open(input_file_path, "r") as json_data:
        data = json.load(json_data)
        message = data["message"]
#loads message in data_1.json
    for key, value in message.items():
        addToSchema(key, value, schema_data)

    with open(output_file_path, "w") as schema_file:
        json.dump(schema_data, schema_file, ensure_ascii=True, indent=4)
#dumps message 
    with open(input_file_path_2, "r") as json_data:
        data = json.load(json_data)
        message = data["message"]
#loads message from data_2.json
    for key, value in message.items():
        addToSchema(key, value, schema_data)

    with open(output_file_path_2, "w") as schema_file:
        json.dump(schema_data, schema_file, ensure_ascii=True, indent=4)
#dumps message       
