import unittest
from ps1 import greedy_cow_transport, cows_dict


class TestCowTransportAlgorithms(unittest.TestCase):


    def test_greedy_cow_transport(self):
        order_of_transport = [["Millie"], ["Maggie", "Milkshake"],
                              ["Moo Moo", "Lola"], ["Florence"]]
        self.assertEqual(greedy_cow_transport(cows_dict, 5), order_of_transport)


    if __name__ == "__main__":
        unittest.main()