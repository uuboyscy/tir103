from datetime import datetime, timedelta

from airflow.decorators import dag, task
from airflow.utils.task_group import TaskGroup

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
    dag_id="d_11_example_import_taskgroup",
    default_args=default_args,
    description="An example DAG with Python operators",
    schedule_interval="* * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
)
def d_11_example_import_taskgroup():
    @task
    def generate_some_str() -> str:
        return "HELLO"

    @task
    def print_something_separately(something: str | list) -> None:
        print("======")
        print(something)
        print("======")

    some_str = generate_some_str()
    result = do_something(some_str)

    # for letter in ["H", "E", "L", "L" "O"]:
    #     print_something(letter)
    with TaskGroup(group_id='do_something_task_group') as do_something_task_group:
        # Dynamically create task instances for processing
        print_something_separately.expand(something=result)

# Instantiate the DAG
d_11_example_import_taskgroup()
