# NYCTaxiAnalysis — Schema Documentation

## Overview

This dataset contains NYC yellow taxi trip data loaded into the bronze layer.

Total rows: ~3,066,766

This represents raw, uncleaned data and may contain anomalies or invalid values.

---

## Table: bronze_trips

### Columns

| Column Name | Type | Description |
|------------|------|-------------|
| VendorID | UInt8 | Taxi vendor identifier (1 or 2) |
| tpep_pickup_datetime | DateTime | Trip start timestamp |
| tpep_dropoff_datetime | DateTime | Trip end timestamp |
| passenger_count | UInt8 | Number of passengers |
| trip_distance | Float32 | Distance traveled (miles) |
| fare_amount | Float32 | Base fare amount |
| tip_amount | Float32 | Tip amount |
| total_amount | Float32 | Total trip cost |

---

## Data Insights

### Vendor Distribution

- Vendor 1: ~827,000 trips (~27%)
- Vendor 2: ~2,239,000 trips (~73%)

Vendor 2 dominates the dataset.

---

### Passenger Count Distribution

- 1 passenger: majority (~2.26M trips)
- 2 passengers: ~451k
- 3+ passengers: decreasing frequency

#### Data Quality Issues:
- Passenger count = 0 → ~122k rows (invalid)
- Passenger count 7–9 → extremely rare (possible anomalies)

---

### Trip Data Observations

- Some trips have:
  - 0 distance
  - 0 fare
  - 0 tip

These likely represent:
- Invalid records
- Test data
- Failed transactions

---

## Data Quality Notes

This is a **bronze layer dataset**, meaning:

- Data is raw and uncleaned
- Contains anomalies and invalid values
- Requires cleaning in the **silver layer**

---

## Next Steps

- Filter invalid rows (e.g. passenger_count = 0)
- Remove or handle zero-distance trips
- Standardize and clean data in materialized views
``
