import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("research_articles.db")

# Load full table
df = pd.read_sql_query("SELECT * FROM Articles_API", conn)

# Export to CSV
df.to_csv("Articles_API.csv", index=False)

conn.close()
print("✅ Exported Articles_API table to Articles_API.csv")