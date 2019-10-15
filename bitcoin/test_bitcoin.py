import bitcoin
import requests
from unittest import TestCase
from unittest.mock import patch, call

class TestBitcoin(TestCase):

    @patch('bitcoin.rate' )
    def test_correct_value_returned(self, mock_rates):
        mock_rate = 1000
        mock_rates.side_effect = [ mock_rate ]
        price = bitcoin.calculate(12)
        self.assertEqual(12000, price)

