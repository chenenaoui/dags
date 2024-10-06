from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

# Define the DAG and its arguments
dag = DAG(
    'simple_dag2',
    description='A simple example DAG',
    schedule_interval='@daily',
    start_date=days_ago(1),
)

# Define tasks
start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

# Set the task sequence
start >> end
