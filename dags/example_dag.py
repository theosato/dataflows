import sys
sys.path.append('/opt/airflow/')

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Import your scripts
from scripts.script1 import script1_function
from scripts.script2 import script2_function
from scripts.script3 import script3_function

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 26),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    description='A simple DAG to run 3 scripts sequentially',
    schedule_interval='@monthly',
    catchup=False
)

task1 = PythonOperator(
    task_id='run_script1',
    python_callable=script1_function,
    dag=dag,
)

task2 = PythonOperator(
    task_id='run_script2',
    python_callable=script2_function,
    dag=dag,
)

task3 = PythonOperator(
    task_id='run_script3',
    python_callable=script3_function,
    dag=dag,
)

task1 >> task2 >> task3
