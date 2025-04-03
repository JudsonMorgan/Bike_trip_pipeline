# 🚴 London Bike Sharing Analytics

## Description
This project aims to create a data pipeline for processing data from the London Bike Rental service (Santander Cycles). The data will be ingested, cleaned, loaded into BigQuery, transformed, and visualized via a dashboard.

## Tech Stack
- **Orchestration:** Apache Airflow
- **Storage:** Google BigQuery
- **Transformation:** dbt (or SQL)
- **Infrastructure:** Terraform 
- **Visualization:** Looker Studio / Metabase 

## Project Structure

### dags/
- **bike_data_pipeline.py**: Airflow DAG to orchestrate the entire data pipeline.
- **dependencies.py**: Shared utility functions for the DAG.
- **load_to_bq.py**: Task to load data to BigQuery.
- **transformation.py**: Task for transforming data for BI usage. 

### scripts/
- **ingest_bike_data.py**: Script to ingest bike rental data.
- **clean_data.py**: Script to clean the ingested data.

### dbt/
- DBT transformation models for cleaning and aggregating the data.

## Setup

1. Clone this repository
    ```
    git clone https://github.com/JudsonMorgan/NYC_trip_data_project.git 
    ```
2. Install dependencies:
    ```
    make setup
    ```
3. Set up Airflow
    ```
    airflow db init
    airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com
    ```
4. Run the Airflow DAG:
    ```
    make run_all
    ```