CREATE OR REPLACE VIEW NYCTaxiAnalysis.gold_what AS
SELECT
    VendorID,
    count(*) AS total_trips,
    avg(fare_amount) AS avg_fare,
    avg(tip_amount) AS avg_tip,
    avg(total_amount) AS avg_total,
    sum(tip_amount) AS total_tips
FROM NYCTaxiAnalysis.silver_trips
GROUP BY VendorID;