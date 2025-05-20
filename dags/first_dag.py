from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'SS',
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='v4',
    default_args=default_args,
    description='1st Dag',
    start_date=datetime(2025, 5, 21, 2, 0),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='task_one',
        bash_command="echo hello world"
    )

    task2 = BashOperator(
        task_id='task_two',
        bash_command="echo hello world 2"
    )

    task3 = BashOperator(
        task_id='task_three',
        bash_command="works with 2"
    )

    task1>>task2
    task1>>task3