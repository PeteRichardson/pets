import unittest
import piku
from pets import Pet
from falcon.testing import TestClient


class TestAPIKey (unittest.TestCase):
    def setUp(self):
        self.keystore = piku.APIKeystore()

    def test_APIKey_exists(self):
        """ APIKey class should have a key property """
        self.assertTrue(hasattr(self.keystore, 'key'))

    def test_keyforuser(self):
        """ key for test should be 4AFC5337-3BCF-4E1D-847E-5F0FA14A7204"""
        key = self.keystore.key("test")
        self.assertEqual(key, '4AFC5337-3BCF-4E1D-847E-5F0FA14A7204')

    def test_keyfornouser(self):
        with self.assertRaises(KeyError):
            dummy_key = self.keystore.key("bogus")


class TestService(unittest.TestCase):

    test_keys = {
        'good': '4AFC5337-3BCF-4E1D-847E-5F0FA14A7204',
        'bad': 'this is not a valid api key'
    }

    def setUp(self):
        self.client = TestClient(piku.service.create())

    def test_pet1(self):
        """ pet #1 should always be Bella         """
        result = self.get_with_auth(TestService.test_keys['good'])
        pet1 = Pet(**result.json)
        self.assertEqual(pet1.name, 'Bella')

    def test_random_pet(self):
        """ random pet should be well formed """
        result = self.client.simulate_get('/pet/random')
        randompet = Pet(**result.json)
        for key in ['name', 'species', 'breed', 'age']:
            # make sure the key exists
            self.assertTrue(hasattr(randompet, key))
            # make sure value isn't empty
            self.assertGreater(len(str(getattr(randompet, key))), 0)

    def get_with_auth(self, apikey):
        params = {
            'headers': {
                'Authorization': apikey
            }
        }
        result = self.client.simulate_get('/pet/1', **params)
        return result

    def test_good_apikey_works(self):
        """ Test that passing a valid API key works  """
        result = self.get_with_auth(TestService.test_keys['good'])
        self.assertEqual(200, result.status_code)

    def test_bad_apikey_fails(self):
        result = self.get_with_auth(TestService.test_keys['bad'])
        self.assertNotEqual(200, result.status_code)

    def test_empty_apikey_fails(self):
        result = self.get_with_auth("")
        self.assertNotEqual(200, result.status_code)

    def test_no_headers_fails(self):
        result = self.get_with_auth(None)
        self.assertNotEqual(200, result.status_code)


if __name__ == "__main__":
    unittest.main()
