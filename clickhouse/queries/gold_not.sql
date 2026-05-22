CREATE OR REPLACE VIEW NYCTaxiAnalysis.gold_not AS
SELECT
    countIf(passenger_count = 0) AS zero_passengers,
    countIf(trip_distance = 0) AS zero_distance,
    countIf(fare_amount = 0) AS zero_fare,
    count(*) AS total_rows
FROM NYCTaxiAnalysis.bronze_trips;
