import pandas as pd

class AssetsAnalysis():
    def __init__(self, filename_day_one, filename_day_two):
        self.df1 = pd.read_csv(filename_day_one)
        self.df2 = pd.read_csv(filename_day_two)

    def top_assets_by_returns(self, df_name, n):
        """
        Find the top N assets based on returns for each country.

        Parameters:
        - n: int, number of assets to retrieve.
        - df_name: str, name of the DataFrame from which to perform the query.

        Returns:
        - pd.DataFrame, DataFrame with the top N assets for each country.
        """
        df = self.df1 if df_name == 'df1' else self.df2
        positive_returns = df[df['RETURN'] > 0].sort_values(by=['COUNTRY','RETURN'], ascending=[True, False]).groupby('COUNTRY').head(n).drop_duplicates()
        negative_returns = df[df['RETURN'] < 0].sort_values(by=['COUNTRY','RETURN'], ascending=[True, False]).groupby('COUNTRY').head(n).drop_duplicates()
        return positive_returns, negative_returns

    def find_missing_assets(self):
        """
        Find assets in self.data but not in other_data.

        Returns:
        - pd.DataFrame, DataFrame with assets in self.df1 but not in self.df2.
        """
        return len(self.df1[~self.df1['AXIOMA_ID'].isin(self.df2['AXIOMA_ID'])])
    
    def top_assets_by_market_cap(self, df_name, n):
        """
    Find the top N assets based on returns for each country.

    Parameters:
    - df_name: str, name of the DataFrame from which to perform the query.
    - n: int, number of assets to retrieve.

    Returns:
    - pd.Series, Series with the top N assets for each country.
    """
        df = self.df1 if df_name == 'df1' else self.df2
        return df.sort_values(by=['COUNTRY','TSO'], ascending=[True, False]).groupby('COUNTRY').head(n).drop_duplicates()
    
    
