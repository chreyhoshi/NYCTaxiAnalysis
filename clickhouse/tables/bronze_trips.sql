CREATE TABLE IF NOT EXISTS NYCTaxiAnalysis.bronze_trips
(
    VendorID UInt8,
    tpep_pickup_datetime DateTime,
    tpep_dropoff_datetime DateTime,
    passenger_count UInt8,
    trip_distance Float32,
    fare_amount Float32,
    tip_amount Float32,
    total_amount Float32
)
ENGINE = MergeTree
ORDER BY tpep_pickup_datetime;