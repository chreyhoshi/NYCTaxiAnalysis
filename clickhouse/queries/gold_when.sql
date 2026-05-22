CREATE OR REPLACE VIEW NYCTaxiAnalysis.gold_when AS
SELECT
    toHour(tpep_pickup_datetime) AS pickup_hour,
    count(*) AS total_trips
FROM NYCTaxiAnalysis.silver_trips
GROUP BY pickup_hour
ORDER BY pickup_hour;