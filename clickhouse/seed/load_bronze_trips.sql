-- NOTE: This ingestion is performed manually for now.
-- In future it should be automated via a data pipeline
-- (e.g. ClickHouse ClickPipes, Airflow, or dlt).

INSERT INTO NYCTaxiAnalysis.bronze_trips
SELECT
    VendorID,
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    passenger_count,
    trip_distance,
    fare_amount,
    tip_amount,
    total_amount
FROM url(
    'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet',
    'Parquet'
);
