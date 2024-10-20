import random
from datetime import datetime, timedelta

from airflow.decorators import dag, task

from tasks.test_tasks import do_something


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
    dag_id="d_10_example_import_tasks",
    default_args=default_args,
    description="An example DAG with Python operators",
    schedule_interval="* * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
)
def d_10_example_import_tasks():
    @task
    def generate_some_str() -> str:
        return "HELLO"

    @task
    def print_something(something: str | list) -> None:
        print("======")
        print(something)
        print("======")

    some_str = generate_some_str()
    result = do_something(some_str)
    print_something(result)

# Instantiate the DAG
d_10_example_import_tasks()
