import pandas as pd 

def clean_data(input_file, output_files):
    """
    Cleans the bike by removing duplicates and handling null values

    Args:
        input file (str): Path to the input file
        output file (str): Path to the output file
    """

    # Load the data
    df = pd.read_json(input_file)

    # Select relevant columns 
    df = df[['id', 'commonName', 'lat', 'lon', 'capacity']]

    # Drop rows where column has null 

    df.dropna(inplace=True)

    # Remove duplicate rows 
    df.drop_duplicates(inplace=True)

    # Save cleaned data to csv
    df.to_csv(output_files, index=False)

    return output_files 

if __name__ == "__main__":
    clean_data("bike_data.json", "cleaned_bike_data.csv")