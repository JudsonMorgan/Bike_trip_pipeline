# 🚴 London Bike Sharing Analytics

## Project Overview
This project processes and analyzes London bike-sharing data using a data pipeline. It ingests, transforms, and visualizes bike usage trends.

## Tech Stack
- **Orchestration:** Apache Airflow
- **Storage:** Google BigQuery
- **Transformation:** dbt (or SQL)
- **Infrastructure:** Terraform 
- **Visualization:** Looker Studio / Metabase 

## Directory Structure
- `dags/` - Airflow DAGs for data pipeline automation
- `dbt/` - Data transformation SQL scripts
- `scripts/` - Data ingestion and cleaning scripts 
- `dashboard/` - Dashboard configuration 
- `terraform/` - Infrastructure setup 
- `tests/` - Unit tests 

## How to Run
1. Clone this repo:
```bash
git clone https://github.com/JudsonMorgan/NYC_trip_data_project.git 

2. Install dependencies:
pip install -r requirements.txt 

3. Run Airflow scheduler:
airflow scheduler

4. View the dashboard on 

