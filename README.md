# JsonSchemaGenerator
A Json Schema Generator

This is a generic program that:

- Reads a JSON file similar to what's present in this location (./data/)
- Sniffs the schema of the JSON file 
- Dumps the output in (./schema/)

The schema output captures ONLY the attributes within the "message" key of the input JSON source data. All attributes withn the key "attributes" were excluded. 
For the json data types:

This program identifies what a string is and map accordingly in the JSON schema output, it also identifies what an integer is and map accordingly in the JSON schema output, it also identifies a string in an array as "enum" and maps the data type as enum and when the value in an array is another JSON object, the program map the data type as an array.

#### Example
From the json data in data_2.json, the data structure is shown below.

{
    "attributes": {
      "appName": "ABCDEFGHIJKLMNOPQRSTUVW",
      "eventType": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
      "subEventType": "ABCDEFGHIJKLMNO",
      "sensitive": false
    },
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
      "internationalCountries":
      [
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
  
  it should generate a json schema as :
      },
    "user": {
        "id": {
            "type": "string",
            "tag": "",
            "description": "",
            "required": false
        },
        "nickname": {
            "type": "string",
            "tag": "",
            "description": "",
            "required": false
        },
        "title": {
            "type": "string",
            "tag": "",
            "description": "",
            "required": false
        },
        "accountType": {
            "type": "string",
            "tag": "",
            "description": "",
            "required": false
        },
        "countryCode": {
            "type": "string",
            "tag": "",
            "description": "",
            "required": false
        },
        "orientation": {
            "type": "string",
            "tag": "",
            "description": "",
            "required": false
        }
    },
    "time": {
        "type": "integer",
        "tag": "",
        "description": "",
        "required": false
    },
    "acl": null,
    "publicFeed": null,
    "internationalCountries": {
        "type": "enum",
        "tag": "",
        "description": "",
        "required": false
    },
    "topTraderFeed": null
}
