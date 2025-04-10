import pandas as pd
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook
from google.cloud import bigquery

def load_to_bq():
    df = pd.read_csv('/Users/judeezeh/Desktop/Zoomcamp-project/data/bike_data.csv')

    # 🔥 FIX: Replace dots in column names (BigQuery doesn't allow them)
    df.columns = df.columns.str.replace('.', '_', regex=False)

    print(f"Processed {df.shape[0]} rows to load into BigQuery.")

    hook = BigQueryHook(gcp_conn_id='google_cloud_default')
    client = hook.get_client()

    table_id = 'zoomcamp-project-455614.NYC_trips_dataset.bike_data'

    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()  # Waits for the job to complete

    print(f"Successfully loaded data to {table_id}.")
