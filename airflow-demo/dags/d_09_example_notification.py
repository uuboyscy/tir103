import random
from datetime import datetime, timedelta

from airflow.decorators import dag, task

from utils.my_notifier import MyNotifier


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
    dag_id="d_09_example_notification",
    default_args=default_args,
    description="An example DAG with Python operators",
    schedule_interval="* * * * *",
    start_date=datetime(2023, 1, 1),
    on_success_callback=MyNotifier(message="Success!"),
    on_failure_callback=MyNotifier(message="Failure!"),
    catchup=False,
    tags=["example", "decorator"]  # Optional: Add tags for better filtering in the UI
)
def d_09_example_notification():
    @task
    def success_or_failure() -> None:
        if random.randint(0,1) == 0:
            print("Failure!")
            raise
        else:
            print("Success!")

    success_or_failure()

# Instantiate the DAG
d_09_example_notification()
