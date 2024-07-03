from airflow import DAG
from datetime import datetime

dag = DAG(
    dag_id='wikipedia_flow',
    default_args={
        'owner':'AJ',
        'start_date': datetime(2024, 6, 28)
    },
    schedule_interval=None,
    catchup=False 
)

# Extraction

# Preprocessing
# Write  