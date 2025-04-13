import unittest
import requests

class TestCheckDeployment(unittest.TestCase):
    def setUp(self):
        self.deployment_url = "http://localhost:5000"

    def test_success(self):
        response = requests.get(self.deployment_url)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
