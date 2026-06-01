import clickhouse_connect, os, json, sys
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

client = clickhouse_connect.get_client(
    host=os.getenv('CLICKHOUSE_HOST'),
    port=int(os.getenv('CLICKHOUSE_PORT', 8443)),
    username=os.getenv('CLICKHOUSE_USER'),
    password=os.getenv('CLICKHOUSE_PASSWORD'),
    secure=True
)

DB = 'NYCTaxiAnalysis'
data = {}

# --- bronze_trips summary ---
result = client.query(f"SELECT count(), min(tpep_pickup_datetime), max(tpep_pickup_datetime) FROM {DB}.bronze_trips")
data['bronze'] = {
    'total_trips': result.result_rows[0][0],
    'min_date': str(result.result_rows[0][1]),
    'max_date': str(result.result_rows[0][2])
}

# --- silver_trips summary ---
result = client.query(f"SELECT count() FROM {DB}.silver_trips")
data['silver'] = {'total_trips': result.result_rows[0][0]}
data['filtered_out'] = data['bronze']['total_trips'] - data['silver']['total_trips']

# --- gold_not (data quality) ---
result = client.query(f"SELECT zero_passengers, zero_distance, zero_fare, total_rows FROM {DB}.gold_not")
row = result.result_rows[0]
data['quality'] = {
    'zero_passengers': row[0],
    'zero_distance': row[1],
    'zero_fare': row[2],
    'total_rows': row[3]
}

# --- gold_what (vendor stats) ---
result = client.query(f"SELECT VendorID, total_trips, avg_fare, avg_tip, avg_total, total_tips FROM {DB}.gold_what ORDER BY VendorID")
data['vendors'] = [
    {'vendor_id': r[0], 'total_trips': r[1], 'avg_fare': round(r[2], 2),
     'avg_tip': round(r[3], 2), 'avg_total': round(r[4], 2), 'total_tips': round(r[5], 2)}
    for r in result.result_rows
]

# --- gold_when (hourly distribution) ---
result = client.query(f"SELECT pickup_hour, total_trips FROM {DB}.gold_when ORDER BY pickup_hour")
data['hourly'] = [[r[0], r[1]] for r in result.result_rows]

# --- gold_extent (daily trend) ---
result = client.query(f"SELECT trip_date, total_trips, total_revenue, avg_revenue FROM {DB}.gold_extent ORDER BY trip_date")
data['daily'] = [
    {'date': str(r[0]), 'total_trips': r[1], 'total_revenue': round(r[2], 2), 'avg_revenue': round(r[3], 2)}
    for r in result.result_rows
]

out_path = os.path.join(os.path.dirname(__file__), 'data.json')
with open(out_path, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Dashboard data saved -> {out_path}")
print(f"  Bronze: {data['bronze']['total_trips']:,}")
print(f"  Silver: {data['silver']['total_trips']:,}")
print(f"  Filtered: {data['filtered_out']:,}")
