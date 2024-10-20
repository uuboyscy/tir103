from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def task1():
    print("Running Task 1")

def task2():
    print("Running Task 2")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'd_01_example_dag',
    default_args=default_args,
    description='An example DAG with Python operators',
    schedule="* * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False
)

# Define the tasks
task1_obj = PythonOperator(
    task_id='task1',
    python_callable=task1,
    dag=dag,
)

task2_obj = PythonOperator(
    task_id='task2',
    python_callable=task2,
    dag=dag,
)

# Task dependencies
task1_obj >> task2_obj

