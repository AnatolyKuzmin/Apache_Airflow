from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="hello_world",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    task1 = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Hello, Airflow!'",
    )

    task2 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    task1 >> task2  # task1.set_downstream(task2)
