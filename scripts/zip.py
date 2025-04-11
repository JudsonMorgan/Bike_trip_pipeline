import os
import zipfile

# Define the project structure and content
files_content = {
    ".gitignore": """
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
venv/
myenv/

# Airflow
airflow/airflow.db
airflow/unittests.cfg

# Sensitive Files
configs/gcp-key.json
.gcp/
.env

# DBT Artifacts
target/
dbt_modules/
logs/

# OS Files
.DS_Store
""",
    ".env": """
GOOGLE_APPLICATION_CREDENTIALS=/Users/judeezeh/.gcp/gcp-key.json
""",
    "SECURITY_CHECKLIST.md": """
# Security Checklist for Zoomcamp Data Pipeline

## Credentials Management
- [x] Service Account Keys are never committed to Git.
- [x] Keys stored locally at ~/.gcp/gcp-key.json
- [x] .gitignore configured to exclude sensitive files.

## GCP Best Practices
- [x] Old service account keys deleted from GCP Console.
- [x] Rotated keys immediately after accidental exposure.

## Local Environment
- [x] Environment variables managed via .env
- [x] Environment variables loaded into Airflow and dbt.

## Git Hygiene
- [x] Used git filter-branch to clean sensitive files from history.
- [x] Forced push cleaned history to GitHub.

## Pipeline Orchestration
- [x] Airflow triggers dbt run after load_to_bq step.
- [x] dbt models structured as staging -> marts.

Stay Secure. Stay Pro.
"""
}

# Create a zip file
output_path = '/Users/judeezeh/Desktop/Zoomcamp-project/zoomcamp_project_package.zip'
with zipfile.ZipFile(output_path, 'w') as zipf:
    for filename, content in files_content.items():
        with open(filename, 'w') as f:
            f.write(content)
        zipf.write(filename)
        os.remove(filename)

output_path
