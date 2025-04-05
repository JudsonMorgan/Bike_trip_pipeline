import pandas as pd

def transform_data_function():
    # Example: Transform data
    bike_df = pd.read_csv('bike_data.csv')  # Assuming bike_data.csv is the file fetched previously
    
    # Example transformation: Clean data, filter, or calculate new columns
    bike_df.dropna(inplace=True)  # Remove rows with missing values
    bike_df['price'] = bike_df['price'].apply(lambda x: x * 1.1)  # Increase price by 10%

    # More transformations based on your needs
    bike_df.to_csv('transformed_bike_data.csv', index=False)
    print("Data transformation completed!")
