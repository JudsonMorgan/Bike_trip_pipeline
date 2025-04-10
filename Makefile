# Makefile for automation 

# Run all tasks in the DAG

run_all:
	airflow dags trigger bike_data_pipeline


# Setup virtual environment and install dependencies 
setup:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt


# Run tests
test:
	pytest tests/


# Start Airflow web server
start_airflow:
	airflow db init
	airflow webserver --port 8080 --worker-class sync &
	airflow scheduler &


# Start Airflow scheduler
start_scheduler:
	airflow scheduler 