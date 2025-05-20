from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import logging

default_args = {
    'owner': 'SS',
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}

def greet():
    name=ti.xcom_pull(task_ids="get_name",key="first_name")
    age=ti.xcom_pull(task_ids="get_age",key="age")
    print(f'Hello World! {name} {age}')


def get_name(ti):
    ti.xcom_push(key="first_name",value="Jerry")

def get_age(ti):
    ti.xcom_push(key="age",value=19)

with DAG(
    dag_id='py_v6',
    default_args=default_args,
    description='1st Dag with python op',
    start_date=datetime(2025, 5, 21, 2, 0),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet_task',
        python_callable=greet
        #op_kwargs={'age':20}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    task2>>task1
    task3>>task1