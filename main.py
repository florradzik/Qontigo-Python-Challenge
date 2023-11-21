from assets import AssetsAnalysis 

assets_analysis = AssetsAnalysis(filename_day_one='universe_2023_09_28.csv', filename_day_two = 'universe_2023_10_04.csv')
top_positive_returns_day_one, top_negative_returns_day_one = assets_analysis.top_assets_by_returns(df_name = 'df1', n=3)
top_market_cap_assets_day_one = assets_analysis.top_assets_by_market_cap('df1', 5)
top_positive_returns_day_two, top_negative_returns_day_two = assets_analysis.top_assets_by_returns(df_name = 'df2', n=3)
top_market_cap_assets_day_two = assets_analysis.top_assets_by_market_cap('df2', 5)

missing_assets = assets_analysis.find_missing_assets()

# Finding the three assets with the largest negative returns for each country

print("Top 3 Assets with Largest Positive Returns for First List:")
print(top_positive_returns_day_one.to_string(index=False, max_rows=None, max_cols=None))

print("Top 3 Assets with Largest Negative Returns for First List:")
print(top_negative_returns_day_one.to_string(index=False, max_rows=None, max_cols=None))

print("Top 3 Assets with Largest Positive Returns for Second List:")
print(top_positive_returns_day_two.to_string(index=False, max_rows=None, max_cols=None))

print("Top 3 Assets with Largest Negative Returns for Second List:")
print(top_negative_returns_day_two.to_string(index=False, max_rows=None, max_cols=None))

print("Top 5 Assets with Largest Market Cap for First List:")
print(top_market_cap_assets_day_one.to_string(index=False, max_rows=None, max_cols=None))

print("Top 5 Assets with Largest Market Cap for Second List:")
print(top_market_cap_assets_day_two.to_string(index=False, max_rows=None, max_cols=None))

print(f"Missing Assets from in 2023-09-28 universe but not in 2023-10-04 universe: {missing_assets}")
