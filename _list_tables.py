import clickhouse_connect, os
from dotenv import load_dotenv
load_dotenv()
client = clickhouse_connect.get_client(
    host=os.getenv('CLICKHOUSE_HOST'),
    port=int(os.getenv('CLICKHOUSE_PORT', 8443)),
    username=os.getenv('CLICKHOUSE_USER'),
    password=os.getenv('CLICKHOUSE_PASSWORD'),
    secure=True
)
databases = client.query('SHOW DATABASES')
print('=== DATABASES ===')
for row in databases.result_rows:
    print(row[0])
print()
tables = client.query("SELECT name, engine FROM system.tables WHERE database = 'default' ORDER BY name")
print('=== TABLES IN default ===')
for row in tables.result_rows:
    print(f'{row[0]} ({row[1]})')
