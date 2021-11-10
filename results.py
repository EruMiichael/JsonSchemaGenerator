
import os

input_file_name= "data_1.json"
input_file_name_2= "data_2.json"

input_file_path = os.path.join(os.curdir, "data", input_file_name)
input_file_path_2 = os.path.join(os.curdir, "data", input_file_name_2)

output_file_name = "schema_1.json"
output_file_path = os.path.join(os.curdir, "schema", output_file_name)

output_file_name_2 = "schema_2.json"
output_file_path_2 = os.path.join(os.curdir, "schema", output_file_name_2)


number_json_schema = """
    {
        "type": "integer",
        "tag": "",
        "description": "",
        "required": false
                       }
"""

string_json_schema = """
    {
        "type": "string",
        "tag": "",
        "description": "",
        "required": false
                       }
"""

array_json_schema = """
    {
        "type": "array",
        "tag": "",
        "description": "",
        "required": false
        }
"""

enum_json_schema = """
    {
        "type": "enum",
        "tag": "",
        "description": "",
        "required": false

    }
"""



json_schema_1='''
    {
    "message": {
      "battle": {
        "id": "ABCDEFGHIJKLMNOPQR",
        "name": "ABCDEFGHIJKLMNOPQRSTUVWX",
        "orientation": "ABCDEFGHIJKLMNO",
        "settings": {
          "minParticipants": 942,
          "maxParticipants": 641,
          "battleType": "ABCDEFGHIJKLMN",
          "wagerType": "ABCDEFGHIJKLMNOPQRSTUVW",
          "countdown": 69,
          "duration": 200,
          "archetype": {
            "name": "ABCDEFGHIJKLMNOPQRS",
            "iconId": "ABCDEFGHIJKLMNOPQRST"
          }
        },
        "status": "ABCDEFGHIJKL",
        "creationTime": 240,
        "startTime": 626,
        "endTime": 353,
        "creator": {
          "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZA",
          "nickname": "ABCDEFGHIJKLMNOPQ",
          "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
          "accountType": "ABCDE",
          "countryCode": "ABCD",
          "orientation": "ABCDEFGHIJKLMNO"
        },
        "participants": [
          {
            "user": {
              "id": "ABCDEFGHIJKLMN",
              "nickname": "ABCDEFGHIJKLMN",
              "title": "ABCDEFGHIJK",
              "accountType": "ABCDEFGHIJKLMNOPQRSTUVWX",
              "countryCode": "ABCDEFGH",
              "orientation": "ABCDEFGHIJKLMNOPQRSTUVWXY"
            },
            "creator": false,
            "ranking": 498,
            "numberOfTrades": 862,
            "performance": "ABCDEFGHIJKLMNOPQRSTUVW"
          }
        ]
      },
      "joiner": {
        "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZAB",
        "nickname": "ABCDEFGHIJKLMNO",
        "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZABC",
        "accountType": "ABCDEFGHIJKLMNOPQRS",
        "countryCode": "ABCDEFGHIJKLMNOPQR",
        "orientation": "ABCDEFGHIJKLMNOPQR"
      },
      "participantIds": [
        "ABCDEFGHIJKLMNOPQRST",
        "ABCDEFGHIJKLMNOPQRSTUVWXY"
      ]
    }
  }
'''
json_schema_2 = """
    {
    "message": {
      "user": {
        "id": "ABCDEFGHIJKLMNOP",
        "nickname": "ABCD",
        "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZABC",
        "accountType": "ABCDEFGHIJKLMNOPQRSTUVWX",
        "countryCode": "ABCDEFGHIJKLMNOPQRSTUVWX",
        "orientation": "ABCDEFGHIJKLMNOPQRSTU"
      },
      "time": 890,
      "acl": [],
      "publicFeed": false,
      "internationalCountries": [
        "ABCDEFGHIJKLMNOPQRSTUVWXYZA",
        "ABCDEFGHIJKLMNOPQ",
        "ABCDEFGHIJKLMNOPQRSTUVW",
        "ABCDEFGHIJKLMNOPQRSTUVWXY",
        "ABCDEFGHIJK",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ABCDEFGHIJKLMNOPQR",
        "ABCDEFG",
        "ABCDEFGHIJKLM"
      ],
      "topTraderFeed": true
    }
  }
"""
