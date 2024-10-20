from datetime import datetime, timedelta

import pandas as pd
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
    dag_id="d_07_example_data_pipeline",
    default_args=default_args,
    description="An example DAG with Python operators",
    schedule_interval="* * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["example", "decorator"]  # Optional: Add tags for better filtering in the UI
)
def d_07_example_data_pipeline():
    @task
    def e_data_source_1() -> pd.DataFrame:
        print("Getting df1.")
        return pd.DataFrame(data=[[1], [2]], columns=["col"])

    @task
    def e_data_source_2() -> pd.DataFrame:
        print("Getting df2.")
        return pd.DataFrame(data=[[3], [4]], columns=["col"])

    @task
    def t_concat(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        print("Concating df1 and df2.")
        return pd.concat([df1, df2]).reset_index(drop=True)
    
    @task
    def l_db1(df: pd.DataFrame) -> None:
        print("Loading df to db1.")
        print(df)
        print("===============")

    @task
    def l_db2(df: pd.DataFrame) -> None:
        print("Loading df to db2.")
        print(df)
        print("===============")

    # Task dependencies defined by calling the tasks in sequence
    df1 = e_data_source_1()
    df2 = e_data_source_2()
    df = t_concat(df1, df2)
    l_db1(df)
    l_db2(df)

# Instantiate the DAG
d_07_example_data_pipeline()
