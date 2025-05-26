import requests
import pandas as pd
from datetime import datetime, timedelta

# === Save Final Dataset ===
df = pd.DataFrame(records)
df.to_csv("adf_pipeline_costs_with_prices.csv", index=False)
print("✔️ Dataset with prices created —", len(df), "rows.")
print(df.head())
