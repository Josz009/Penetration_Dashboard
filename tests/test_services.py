
import unittest
from app.services.nmap_service import run_nmap_scan

class TestNmapService(unittest.TestCase):
    def test_run_nmap_scan(self):
        results = run_nmap_scan("127.0.0.1", "-sV")
        self.assertIsInstance(results, list)

if __name__ == "__main__":
    unittest.main()
