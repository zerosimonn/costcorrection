import unittest
from settings import inflation_df

class TestInflationData(unittest.TestCase):
    # Test to ensure that the inflation data has the same number of years and rates
    def test1(self):
        """Test to ensure that the inflation data has the same number of years and rates"""
        self.assertEqual(
            len(inflation_df['year']), len(inflation_df['rate'])
        )

    # Test to ensure that the years are in the expected order
    def test2(self):
        """Test to ensure that the years are in the expected order"""
        self.assertEqual(
            inflation_df['year'].tolist(), list(range(2010, 2027))
        )

    # Test to ensure that the rates are all non-negative
    def test3(self):
        """Test to ensure that the rates are all non-negative
        /n"""
        self.assertTrue(
            all(rate >= 0 for rate in inflation_df['rate'])
        )

if __name__ == '__main__':
    unittest.main(verbosity=1)