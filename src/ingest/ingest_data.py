import os
import pandas as pd
import mysql.connector
import json


# Path to config/db_config.json
CONFIG_PATH = os.path.join(os.path.dirname(__file__),"..", "..", "config", "db_config.json")

with open(CONFIG_PATH, "r") as f:
    DB_CONFIG = json.load(f)

def ingest_data():
    # Load JSON
    json_path = os.path.join("data/gold", "porter_data_transformed.json")
    df = pd.read_json(json_path)

    # Connect to MySQL
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Load schema from file
    schema_path = os.path.join("config", "schema.sql")
    with open(schema_path, "r") as f:
        schema_sql = f.read()
    cursor.execute(schema_sql)

    # Insert data
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO porter_data (
                market_id, created_at, actual_delivery_time, store_primary_category, 
                order_protocol, total_items, subtotal, num_distinct_items, min_item_price, 
                max_item_price, total_onshift_dashers, total_busy_dashers, total_outstanding_orders, 
                estimated_store_to_consumer_driving_duration, delivery_duration_mins, avg_item_price, 
                dasher_utilization, orders_per_dasher, order_date, order_hour, day_of_week
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["market_id"],
            row["created_at"],
            row["actual_delivery_time"],
            row["store_primary_category"],
            row["order_protocol"],
            row["total_items"],
            row["subtotal"],
            row["num_distinct_items"],
            row["min_item_price"],
            row["max_item_price"],
            row["total_onshift_dashers"],
            row["total_busy_dashers"],
            row["total_outstanding_orders"],
            row["estimated_store_to_consumer_driving_duration"],
            row["delivery_duration_mins"],
            row["avg_item_price"],
            row["dasher_utilization"],
            row["orders_per_dasher"],
            row["order_date"],
            row["order_hour"],
            row["day_of_week"]
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Data ingestion complete!")


if __name__ == "__main__":
    ingest_data()
