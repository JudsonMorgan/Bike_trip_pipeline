from airflow.hooks.base_hook import BaseHook
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook

def get_gcs_connection():
    connection = BaseHook.get_connection('google_cloud_storage')
    return connection 


def get_bq_connection():
    return BigQueryHook(gcp_conn_id='google_cloud_default')