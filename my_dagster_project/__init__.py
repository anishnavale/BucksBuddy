from dagster import Definitions, load_assets_from_modules
from dagstermill import local_output_notebook_io_manager

from . import assets, schedules, jobs


all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    jobs=[jobs.run_StockData_job],
    schedules=[schedules.everyday_11pm],
    resources={
        "output_code_io_manager": local_output_notebook_io_manager,
        "output_notebook_io_manager": local_output_notebook_io_manager
    }
)

