"""
CLI command:
airflow dags trigger -c '{"start_date": "2024-01-01", "end_date": "2024-03-01"}' d_06_example_pass_parameters_cli
airflow dags test -c '{"start_date": "2024-01-01", "end_date": "2024-03-01"}' d_06_example_pass_parameters_cli
"""
from datetime import datetime

from airflow.decorators import dag, task

# Default values for start_date and end_date
DEFAULT_START_DATE = "2023-01-01"
DEFAULT_END_DATE = "2023-12-31"

@dag(
    dag_id="d_06_example_pass_parameters_cli",
    schedule_interval=None,  # Set to None for manual triggering
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["example", "cli_variables_defaults"]
)
def d_06_example_pass_parameters_cli():
    @task
    def extract_parameters(ti):
        # some_args = ti.xcom_pull(task_ids='trigger', key='return_value')
        # if some_args:
        #     config = some_args
        # else:
        #     config = {}
        config = ti.xcom_pull(task_ids='trigger', key='return_value') or {}
        # Get parameters with defaults if not provided via CLI
        start_date = config.get('start_date', DEFAULT_START_DATE)
        end_date = config.get('end_date', DEFAULT_END_DATE)
        return {"start_date": start_date, "end_date": end_date}

    @task
    def start_task(date_params):
        # This task can use the start_date and end_date directly
        print(f"Task runs with a start date of {date_params.get('start_date')} and end date of {date_params.get('end_date')}")

    date_params = extract_parameters()
    start_task(date_params)

# Create the DAG instance
d_06_example_pass_parameters_cli()
