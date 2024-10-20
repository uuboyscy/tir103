from datetime import datetime, timedelta

from airflow.decorators import dag, task

from utils.testutils import testfunc


# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["your_email@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    dag_id="d_08_example_import_utils",
    default_args=default_args,
    description="An example DAG with Python operators",
    schedule_interval="* * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["example", "decorator"]  # Optional: Add tags for better filtering in the UI
)
def d_08_example_import_utils():
    @task
    def call_custom_utils() -> None:
        testfunc()

    # Task dependencies defined by calling the tasks in sequence
    call_custom_utils()

# Instantiate the DAG
d_08_example_import_utils()
