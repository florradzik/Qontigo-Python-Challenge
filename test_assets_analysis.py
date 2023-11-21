import pandas as pd
import numpy as np
import unittest
import os
from assets import AssetsAnalysis

# Define a function to create sample data

DATA_PATH_DAY_ONE = 'sample_data_day_one.csv'
DATA_PATH_DAY_TWO = 'sample_data_day_two.csv'

class TestAssetsAnalysis(unittest.TestCase):
    def create_sample_data(self, num_assets=100, countries=['USA', 'Canada', 'UK']):
        np.random.seed(42)  # For reproducibility

        # Generate synthetic data for df1
        df1_data = {
            'AXIOMA_ID': np.arange(1, num_assets + 1),
            'COUNTRY': np.random.choice(countries, size=num_assets),
            'RETURN': np.random.uniform(-0.1, 0.1, size=num_assets),
            'TSO': np.random.randint(100000, 1000000, size=num_assets)
        }
        df1 = pd.DataFrame(df1_data)

        # Generate synthetic data for df2
        df2_data = {
            'AXIOMA_ID': np.arange(num_assets + 1, 2 * num_assets + 1),
            'COUNTRY': np.random.choice(countries, size=num_assets),
            'RETURN': np.random.uniform(-0.1, 0.1, size=num_assets),
            'TSO': np.random.randint(100000, 1000000, size=num_assets)
        }
        df2 = pd.DataFrame(df2_data)

        df1.to_csv(DATA_PATH_DAY_ONE, index=False)
        df2.to_csv(DATA_PATH_DAY_TWO, index=False)

    def tearDown(self):
        def tearDown(self):
        # Remove the sample data files after the tests
            if os.path.exists(DATA_PATH_DAY_ONE):
                os.remove(DATA_PATH_DAY_ONE)
            if os.path.exists(DATA_PATH_DAY_TWO):
                os.remove(DATA_PATH_DAY_TWO)
            
    def setUp(self):
        self.create_sample_data()
        self.assets_analysis_instance = AssetsAnalysis(filename_day_one=DATA_PATH_DAY_ONE, filename_day_two=DATA_PATH_DAY_TWO)

    def test_top_assets_by_returns(self):
        # Test top assets by returns for df1
        positive_returns_df1, negative_returns_df1 = self.assets_analysis_instance.top_assets_by_returns(df_name='df1', n=3)
        self.assertEqual(len(positive_returns_df1), 9)
        self.assertEqual(len(negative_returns_df1), 9)

        # Test top assets by returns for df2
        positive_returns_df2, negative_returns_df2 = self.assets_analysis_instance.top_assets_by_returns(df_name='df2', n=3)
        self.assertEqual(len(positive_returns_df2), 9)
        self.assertEqual(len(negative_returns_df2), 9)

    def test_find_missing_assets(self):
        missing_assets = self.assets_analysis_instance.find_missing_assets()
        self.assertIsInstance(missing_assets, int)

    def test_top_assets_by_market_cap(self):
        # Test top assets by market cap for df1
        top_market_cap_df1 = self.assets_analysis_instance.top_assets_by_market_cap(df_name='df1', n=5)
        self.assertEqual(len(top_market_cap_df1), 15)

        # Test top assets by market cap for df2
        top_market_cap_df2 = self.assets_analysis_instance.top_assets_by_market_cap(df_name='df2', n=5)
        self.assertEqual(len(top_market_cap_df2), 15)

if __name__ == '__main__':
    unittest.main()
