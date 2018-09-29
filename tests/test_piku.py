import unittest
import piku

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
            key = self.keystore.key("bogus")

if __name__ == "__main__":
    unittest.main()