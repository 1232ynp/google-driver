from my_lib import fetcher
from my_lib import inserter
import datetime
import os


def main(event, context):
    # 現在の日付を取得
    cur_date = str(datetime.datetime.now().date())

    try:
        # 最高風速を取得
        cur_max_wind_speed_df = fetcher.fetch_max_wind_speed(cur_date)
        # 最高気温を取得
        cur_max_temperature_df = fetcher.fetch_max_temperature(cur_date)

        # データをBigQueryにinsert
        cur_max_wind_speed_table_schema = [
            {'name': 'date', 'type': 'DATE'},
            {'name': 'place', 'type': 'STRING'},
            {'name': 'daily_max_wind_speed', 'type': 'FLOAT'},
        ]
        inserter.insert_bq(cur_max_wind_speed_df,
                           os.environ["BQ_DATASET_NAME_WHETHER"] + ".max_wind_speed",
                           "nari-training",
                           cur_max_wind_speed_table_schema)

        # データをBigQueryにinsert
        cur_max_temperature_table_schema = [
            {'name': 'date', 'type': 'DATE'},
            {'name': 'place', 'type': 'STRING'},
            {'name': 'daily_max_temperature', 'type': 'FLOAT'},
        ]

        inserter.insert_bq(cur_max_temperature_df,
                           os.environ["BQ_DATASET_NAME_WHETHER"] + ".max_temperature",
                           "nari-training",
                           cur_max_temperature_table_schema)

    except Exception as err:
        print("Overview ： " + str(type(err)))
        print("Details  ： " + str(err))
