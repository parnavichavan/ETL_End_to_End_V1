import pandas as pd
import os

# Paths
INPUT_PATH = "/data/raw/porter_data.csv"
OUTPUT_DIR = "./data/gold"
OUTPUT_EXCEL = os.path.join(OUTPUT_DIR,"porter_data_transformed.xlsx")
OUTPUT_JSON = os.path.join(OUTPUT_DIR,"porter_data_transformed.json")

def transform_data():
    df = pd.read_csv(INPUT_PATH, parse_dates=["created_at", "actual_delivery_time"])

    # 2. Handle missing values
    df = df.dropna(subset=["created_at", "actual_delivery_time"])  # critical timestamps
    df = df.fillna(0)  # fill other numeric nulls with 0

    # 3. Derived features
    df["delivery_duration_mins"] = (df["actual_delivery_time"] - df["created_at"]).dt.total_seconds() / 60
    df["avg_item_price"] = df["subtotal"] / df["total_items"].replace(0, 1)  # avoid div/0
    df["dasher_utilization"] = df["total_busy_dashers"] / df["total_onshift_dashers"].replace(0, 1)
    df["orders_per_dasher"] = df["total_outstanding_orders"] / df["total_onshift_dashers"].replace(0, 1)

    # 4. Feature Engineering – date parts
    df["order_date"] = df["created_at"].dt.date
    df["order_hour"] = df["created_at"].dt.hour
    df["day_of_week"] = df["created_at"].dt.day_name()

    # 5. Save outputs
    df.to_excel(OUTPUT_EXCEL, index=False)
    df.to_json(OUTPUT_JSON, orient="records", indent=4, date_format="iso")

    print(f"Transformation complete. Files saved to {OUTPUT_EXCEL} and {OUTPUT_JSON}")

if __name__ == "__main__":
    transform_data()
