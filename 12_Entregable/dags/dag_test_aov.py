from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from etlpy import cryptoetl
default_args={
    'owner':'Alexander',
    'retries':5,
    'retry_delay':timedelta(minutes=1),
    'start_date':days_ago(0)

}

ingestion_dag = DAG(
    dag_id='test_aov',
    default_args=default_args,
    description='testing',
    schedule_interval = '@daily',
    catchup=False,
)

task1 = BashOperator(
    task_id='Start_DAG',
    bash_command='echo Iniciando DAG',
    dag=ingestion_dag,
    )
task2 = PythonOperator(
    task_id='Conectar_redshift',
    python_callable=cryptoetl.conectar_Redshift, 
    provide_context=True,  
    dag=ingestion_dag,
)
task3 = PythonOperator(
    task_id='Extraer_data',
    python_callable=cryptoetl.extract, 
    provide_context=True,  
    dag=ingestion_dag,
)
task4= PythonOperator(
    task_id='Transformar_data',
    python_callable=cryptoetl.transform,
    provide_context=True,
    dag=ingestion_dag,
)
task5= PythonOperator(
    task_id='Cargar_Redshift',
    python_callable=cryptoetl.load2rds,
    provide_context=True,
    dag=ingestion_dag,
)
task6= PythonOperator(
    task_id='Enviar_mail',
    python_callable=cryptoetl.sendmail,
    provide_context=True,
    dag=ingestion_dag,
)
task7= BashOperator(
    task_id='Finalizando_DAG',
    bash_command='echo Finalizando DAG',
    dag=ingestion_dag,
)
task1 >> task2 >> task3 >> task4 >> task5 >> task6 >>task7