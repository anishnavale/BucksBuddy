from dagster import ScheduleDefinition
from . import jobs

everyday_11pm = ScheduleDefinition(
    job = jobs.run_StockData_job,
    cron_schedule= "0 23 * * * ",
    execution_timezone="America/New_York",
)