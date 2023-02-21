SELECT TIMESTAMP(date) as datetime, place, daily_max_wind_speed AS timestamp_date
FROM `nari-training.whether_db.max_wind_speed`
where date = CURRENT_DATE()