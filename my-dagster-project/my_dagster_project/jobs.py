from . import assets
from dagster import (
    define_asset_job,
    AssetSelection
)

run_StockData_job = define_asset_job("run_StockData_job", AssetSelection.groups("Code"))