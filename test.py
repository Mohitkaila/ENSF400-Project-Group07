import unittest
import requests

class TestCheckDeployment(unittest.TestCase):
    def setUp(self):
        self.deployment_url = "http://localhost:5000"
    
    def test_success(self):
        try:
            response = requests.get(self.deployment_url)
            self.assertEqual(response.status_code, 200)
        except requests.exceptions.RequestException as e:
            self.fail(f"Deployment failed: {e}")
    
    def test_failure(self):
        try:
            response = requests.get("http://invalid-url.com")
            self.assertNotEqual(response.status_code, 200)
        except requests.exceptions.RequestException as e:
            self.fail(f"Request failed: {e}")

if __name__ == "__main__":
    unittest.main()

