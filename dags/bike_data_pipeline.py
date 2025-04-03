from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime 


from dags.dependencies import get_bq_connection 
from scripts.ingest_bike_data import ingest_bike_data
from scripts.clean_data import clean_data
from dags.load_to_bq import load_to_bq 
from dags.transformation import transformation 


# Define the DAG 

dag = DAG(
    'bike_data_pipeline',
    default_args={
        'owner' : 'airflow',
        'start_date': datetime(2023, 1, 1),
        'retries': 1,
    },
    description='A simple bike data pipeline',
    schedule_interval=None,
)


# Defining the tasks
task_1 = PythonOperator(
    task_id = 'ingest_bike_data',
    python_callable=ingest_bike_data,
    dag=dag,
)

task_2 = PythonOperator(
    task_id = 'clean_data',
    python_callable=clean_data,
    op_args=['bike_data.json', 'cleaned_bike_data.csv'],
    dag=dag,
)

task_3 = PythonOperator(
    task_id = 'load_to_bq',
    python_callable=load_to_bq,
    dag=dag,
)

task_4 = PythonOperator(
    task_id = 'transformation',
    python_callable=transformation,
    dag=dag,
)


task_1 >> task_2 >> task_3 >> task_4