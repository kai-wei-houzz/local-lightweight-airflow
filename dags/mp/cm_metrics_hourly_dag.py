from datetime import datetime
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping, SparkThriftProfileMapping

# from include.profiles import airflow_db
# from include.constants import jaffle_shop_path, venv_execution_config

dbt_path = '/opt/airflow/dags/dags/dbt'
dbt_exec_path = '/Users/kwliao/Development/airflow_dbt/.airflow_dbt/bin/dbt'
profile_config = ProfileConfig(
    profile_name="mp_metrics_hourly",
    target_name="dev",
    profiles_yml_filepath="/Users/kwliao/Development/airflow_dbt/dags/dbt/"
    # profile_mapping=SparkThriftProfileMapping(
    #     conn_id="spark_default",
    #     profile_args={"schema": "public"},
    # ),
)

simple_dag = DbtDag(
    # dbt/cosmos-specific parameters
    # project_config=ProjectConfig(jaffle_shop_path),
    project_config=ProjectConfig(f"{dbt_path}/mp_metrics_hourly"),
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path=dbt_exec_path,
    ),
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="simple_dag",
    tags=["simple"],
)