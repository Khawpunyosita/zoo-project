import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_negative_age_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)

    def test_0_to_12_age_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_13_to_20_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_21_to_60_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
    
    def test_more_than_60_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
    
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()