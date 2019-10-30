from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from dsutil import NbExecuter

# Define default args
default_args = {
    'owner': 'user',
    'on_failure_callback': lambda context: True
}    

# Define DAG setting
dag = DAG('Sponge City Overflow Evaluation', description='Scheduled task ',
          schedule_interval='*/5 * * * *',
          start_date=datetime(2019, 1, 1), 
          default_args=default_args,
		  dagrun_timeout=timedelta(seconds=30),
          catchup=False)

# Define DAG components
sandboxNotebook = PythonOperator(
    task_id='Sandbox',
    python_callable=NbExecuter.OverflowServiceSandbox,
    provide_context=True,
    op_kwargs={'path': "papermill OverflowServiceSandbox.ipynb ./OverflowServiceSandbox_run_cli.ipynb -p start '2019-06-04T0:55:52Z' -p stop '2019-06-05T19:28:52Z' -p levelThreshold 0.45 -p maxThreshold 0.90 -p levelSlopeAngle 0.000085 -p dataOffset 0 -p bufferLength 30 -p resultAttribute 'overflow'"},
    dag=dag
)

productionNotebook = PythonOperator(
    task_id='Production',
    python_callable=NbExecuter.OverflowServiceSandbox,
    provide_context=True,
    op_kwargs={'path': "papermill OverflowServiceSandbox.ipynb ./OverflowServiceSandbox_run_cli.ipynb -p start '2019-06-04T0:55:52Z' -p stop '2019-06-05T19:28:52Z' -p levelThreshold 0.45 -p maxThreshold 0.90 -p levelSlopeAngle 0.000085 -p dataOffset 0 -p bufferLength 30 -p resultAttribute 'overflow'"},
    dag=dag
)


# Define dependencies
sandboxNotebook >> productionNotebook