SELECT TIMESTAMP(date) as datetime, place, daily_max_temperature AS timestamp_date
FROM `nari-training.whether_db.max_temperature`
where date = CURRENT_DATE()