from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook

def get_bq_hook():
    return BigQueryHook(gcp_conn_id='google_cloud_default')
