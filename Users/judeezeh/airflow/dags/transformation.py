import pandas as pd

def process_bike_data():
    df = pd.read_csv('/data/bike_data_raw.csv')

    # Handle missing columns gracefully
    for col in ['location.city', 'location.country']:
        if col not in df.columns:
            df[col] = ''

    df['location'] = df['location.city'] + ', ' + df['location.country']
    cleaned_df = df[['id', 'name', 'location']]

    cleaned_df.to_csv('/data/bike_data_clean.csv', index=False)

