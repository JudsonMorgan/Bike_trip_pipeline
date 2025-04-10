from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from fetch_bike_data import fetch_data
from transformation import process_bike_data
from load_to_bq import load_to_bq

with DAG(
    'bike_data_pipeline',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['bike', 'ETL'],
) as dag:

    t1 = PythonOperator(task_id='fetch_bike_data', python_callable=fetch_data)
    t2 = PythonOperator(task_id='process_bike_data', python_callable=process_bike_data)
    t3 = PythonOperator(task_id='load_to_bq', python_callable=load_to_bq)

    t1 >> t2 >> t3
