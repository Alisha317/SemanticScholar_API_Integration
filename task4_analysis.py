import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("research_articles.db")
cursor = conn.cursor()

# 1. Top 5 most-cited papers
print("\n📌 Top 5 Most-Cited Papers:")
cursor.execute("""
SELECT Title, CitationCount
FROM Articles_API
ORDER BY CitationCount DESC
LIMIT 5;
""")
for row in cursor.fetchall():
    print(row)

# 2. Count papers published per year
print("\n📌 Papers Published Per Year:")
cursor.execute("""
SELECT Year, COUNT(*) AS PaperCount
FROM Articles_API
GROUP BY Year
ORDER BY Year;
""")
for row in cursor.fetchall():
    print(row)

# 3. Authors with more than 1 publication
print("\n📌 Authors with More Than 1 Publication:")
cursor.execute("""
SELECT Authors, COUNT(*) AS NumPublications
FROM Articles_API
GROUP BY Authors
HAVING COUNT(*) > 1;
""")
for row in cursor.fetchall():
    print(row)

# 4. Papers that share a common reference (exact match of Reference_List)
print("\n📌 Papers that Share a Common Reference:")
cursor.execute("""
SELECT a.PaperID, a.Title, a.Reference_List
FROM Articles_API a
JOIN Articles_API b
  ON a.PaperID <> b.PaperID
 AND a.Reference_List = b.Reference_List
LIMIT 10;
""")
for row in cursor.fetchall():
    print(row)

conn.close()