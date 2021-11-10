'''
This is code is a unittest, it tests the main.py code for errors
'''

import unittest
import json, sys
from main import getSchema,schema_data, message, input_file_name, input_file_name_2, input_file_path, input_file_path_2, output_file_name, output_file_path, output_file_name_2, output_file_path_2, addToSchema
import results



class TestSchemaGenerator(unittest.TestCase):

#The function test for the corect filename
        def test_input_filename_1(self):
                outcome = input_file_name
                result = results.input_file_name
            
                self.assertEqual(outcome, result)

#The function test for the corect filename                 
        def test_input_filename_2(self):
                outcome = input_file_name_2
                result =results.input_file_name_2
            
                self.assertEqual(outcome, result)

#The function test for the corect file path
        def test_input_file_path_1(self):
                outcome = input_file_path
                result = results.input_file_path
            
                self.assertEqual(outcome, result)

#The function test for the corect file path
        def test_input_file_path_2(self):
                outcome = input_file_path_2
                result =results.input_file_path_2
            
                self.assertEqual(outcome, result)
                
#The function test for the corect filename            
        def test_output_filename(self):
                outcome = output_file_name
                result=results.output_file_name
            
                self.assertEqual(outcome, result)

#The function test for the corect filename
        def test_output_filename_2(self):
                outcome = output_file_name_2
                result =results.output_file_name_2
            
                self.assertEqual(outcome, result)

#The function test for the corect file path
        def test_output_file_path(self):
                outcome = output_file_path
                result = results.output_file_path
            
                self.assertEqual(outcome, result)

#The function test for the corect file path
        def test_output_file_path_2(self):
                outcome = output_file_path_2
                result = results.output_file_path_2
            
                self.assertEqual(outcome, result)
#The function test for integers             
        def test_for_number(self):
                outcome = getSchema(1)
                result = json.loads(results.number_json_schema)
            
                self.assertEqual(outcome, result)

#The function test strings

        def test_fot_strings(self):
                outcome = getSchema('"str"')
                result = json.loads(results.string_json_schema)

                self.assertEqual(outcome, result)

#The function test for enum                
        def test_for_enum(self):
                
                outcome = getSchema(["string_1","string_2"])
                result = json.loads(results.enum_json_schema)

                self.assertEqual(outcome, result)
                
#The function test for an array                 
        def test_for_array(self):
        
                outcome = getSchema([{"key_1": "value_1"}])
                result = json.loads(results.array_json_schema)

                self.assertEqual(outcome, result)


if __name__ == '__main__':
        unittest.main()
