CREATE OR REPLACE VIEW NYCTaxiAnalysis.gold_extent AS
SELECT
    toDate(tpep_pickup_datetime) AS trip_date,
    count(*) AS total_trips,
    sum(total_amount) AS total_revenue,
    avg(total_amount) AS avg_revenue
FROM NYCTaxiAnalysis.silver_trips
GROUP BY trip_date
ORDER BY trip_date;
