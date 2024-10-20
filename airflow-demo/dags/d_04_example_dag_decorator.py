import pendulum
from airflow.decorators import dag, task, bash_task


# Define the DAG
@dag(
    schedule="* * * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def d_04_example_dag_decorator():
    @task
    def task1():
        print("Running Task 1")
    @task
    def task2():
        print("Running Task 2")

    @bash_task
    def task3():
        return "echo 'Hello from Task 3!'"

    t1 = task1()
    task2().set_upstream(t1)
    task3().set_upstream(t1)

d_04_example_dag_decorator()
