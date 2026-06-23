import pandas as pd
from sqlalchemy import create_engine

# Read cleaned file
df = pd.read_csv("clean_superstore.csv")

# Created PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:mynewpassword@localhost:5432/retail_analytics"
)

# Load data into PostgreSQL
df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully.")