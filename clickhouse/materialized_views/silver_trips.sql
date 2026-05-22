CREATE MATERIALIZED VIEW IF NOT EXISTS NYCTaxiAnalysis.silver_trips
ENGINE = MergeTree
ORDER BY tpep_pickup_datetime
AS
SELECT
    VendorID,
    tpep_pickup_datetime,
    tpep_dropoff_datetime,

    passenger_count,

    trip_distance,

    fare_amount,
    tip_amount,
    total_amount

FROM NYCTaxiAnalysis.bronze_trips

WHERE
    passenger_count > 0
    AND trip_distance > 0
    AND fare_amount > 0;
