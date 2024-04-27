from dagster import file_relative_path
from dagstermill import define_dagstermill_asset

PredData = define_dagstermill_asset(
    name="Stock_Data",
    notebook_path=file_relative_path(__file__, "/Users/anishnavale/Desktop/GenAI Project/project/my-dagster-project/my_dagster_project/Code/PredData.ipynb"),
    group_name="Code",
    io_manager_key="output_code_io_manager"
)

LLM_Phase1 = define_dagstermill_asset(
    deps= [PredData],
    name="LLM_Phase1",
    notebook_path=file_relative_path(__file__, "/Users/anishnavale/Desktop/GenAI Project/project/my-dagster-project/my_dagster_project/Code/LLM1.ipynb"),
    group_name="Code",
    io_manager_key="output_notebook_io_manager"
)
