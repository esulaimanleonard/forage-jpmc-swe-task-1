import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        expected_data_points = [
            ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]
        for quote, expected in zip(quotes, expected_data_points):
            self.assertEqual(getDataPoint(quote), expected)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        expected_data_points = [
            ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]
        for quote, expected in zip(quotes, expected_data_points):
            self.assertEqual(getDataPoint(quote), expected)

    def test_getRatio(self):
        # Test normal ratio calculation
        price_a = 120.84
        price_b = 122.09
        expected_ratio = price_a / price_b
        self.assertEqual(getRatio(price_a, price_b), expected_ratio)
        
        # Test ratio when price_b is zero
        self.assertIsNone(getRatio(price_a, 0))
        
        # Test ratio when price_a is zero
        self.assertEqual(getRatio(0, price_b), 0)

if __name__ == '__main__':
    unittest.main()
