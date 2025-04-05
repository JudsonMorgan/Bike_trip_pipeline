from google.cloud import bigquery 
import pandas as pd 

def load_to_bq(file_path):
    # Initialize BigQuery client 

    client = bigquery.Client()

    # Load the cleaned CSV file into BigQuery
    df = pd.read_csv(file_path)
    table_id = "zoomcamp-project-455614.NYC_trips_dataset"

    # Upload to BigQuery
    job = client.load_table_from_dataframe(df, table_id)
    job.result()

    return f"Data loaded to BigQuery: {table_id}"