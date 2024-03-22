from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import timedelta
import pendulum


start_date = pendulum.datetime(2024, 3, 19, tz="UTC")


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    'eks_deployment_automation',
    start_date=start_date,
    default_args=default_args,
    description='Automate EKS deployment and log retrieval with Airflow',
)


deploy_task = BashOperator(
    task_id='deploy_application',
    bash_command='kubectl apply -f eks_deployement/deployment.yaml',
    dag=dag,
)


get_logs_task = BashOperator(
    task_id='get_pod_logs',
    bash_command='kubectl logs $(kubectl get pods -l app=poc-jupitermoney -o jsonpath="{.items[0].metadata.name}")',
    dag=dag,
)


deploy_task >> get_logs_task
