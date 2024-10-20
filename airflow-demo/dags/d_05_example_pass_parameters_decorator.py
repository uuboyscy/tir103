from datetime import datetime, timedelta

from airflow.decorators import dag, task


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
    dag_id="d_05_example_pass_parameters_decorator",
    default_args=default_args,
    description="An example DAG with Python operators",
    schedule_interval="* * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["example", "decorator"]  # Optional: Add tags for better filtering in the UI
)
def d_05_example_pass_parameters_decorator():
    @task
    def task1():
        print("Running Task 1")
        return "Hello from Task 1!"

    @task
    def task2(returned_value_from_task1):
        print("Running Task 2")
        print(f"Received from Task 1: {returned_value_from_task1}")

    # Task dependencies defined by calling the tasks in sequence
    result_from_task1 = task1()
    task2(result_from_task1)

# Instantiate the DAG
d_05_example_pass_parameters_decorator()
