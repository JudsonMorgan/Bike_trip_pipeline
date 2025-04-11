# Zoomcamp Data Engineering Project

Modern Data Pipeline for NYC Bike Data using:

- Apache Airflow (Orchestration)
- Google BigQuery (Data Warehouse)
- dbt (Transformations & Analytics)
- Secure Environment & Production-Ready Setup

---

---

## Setup Instructions

### 1. Clone This Repository:

```bash
git clone [Github repo](https://github.com/JudsonMorgan/NYC_trip_data_project)
cd zoomcamp_project
```

### 2. Create Virtual Environment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 3. Environment variable

`GOOGLE_APPLICATION_CREDENTIALS=/Users/<your-username>/.gcp/gcp-key.json`

Load it:
```bash
export $(cat .env | xargs)
```

### 4. Running Airflow Locally

```bash
airflow db init
airflow scheduler
airflow webserver
```

Trigger DAG:
```bash
airflow dags trigger bike_data_pipeline
```
### 5. Running dbt locally

Navigate to your dbt project:
```bash
cd my_project/
dbt debug
dbt run
dbt test
dbt docs generate
dbt docs serve
```

### Security Notes
- GCP Keys are NEVER committed to Git.

- Secrets managed via `.env`

- `.gitignore` protects sensitive files.

- Refer to `SECURITY_CHECKLIST.md` for best practices.


Author
Built with ❤️ by Jude — powered by Airflow, BigQuery, and dbt.