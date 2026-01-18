import unittest
from settings import inflation_df

class TestInflationData(unittest.TestCase):
    def test_inflation_data_length(self):
        self.assertEqual(
            len(inflation_df['year']), len(inflation_df['rate'])
        )

if __name__ == '__main__':
    unittest.main()
