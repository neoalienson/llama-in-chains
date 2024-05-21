import unittest
from unittest.mock import patch
import config

class TestReadConfig(unittest.TestCase):
    def side_effect(self, value):
        print('side effect')
        print(value)
        return value

    @patch('pyaml_env.parse_config')
    # @patch('os.path.isfile')
    # @patch('pyaml_env.parse_config')    
    def test_read_config_defaults(self, mock_parse_config):
        print(mock_parse_config)
        # print(mock_parse_config2)        
        # Mock the result of `parse_config('default.yaml')`
        mock_parse_config.return_value = {'key': 'value'}
        mock_parse_config.side_effect= side_effect
        # mock_parse_config2.return_value = {'key': 'value'}        


        # Mock the result of `os.path.isfile('config.yaml')` to return False
        # mock_isfile.return_value = False
        
        # # Call the function being tested
        result = config.read_config()
        print(result.gradio_server_name)
        
        # # Assert that the returned configuration is as expected
        self.assertEqual(result.key, 'value')

if __name__ == '__main__':
    unittest.main()