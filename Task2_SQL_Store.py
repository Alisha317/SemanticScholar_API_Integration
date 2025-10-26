import requests
import sqlite3

# Define the API endpoint and parameters
url = "https://api.semanticscholar.org/graph/v1/paper/search"
params = {
    "query": "artificial intelligence in education",
    "limit": 20,
    "fields": "title,authors,abstract,year,citationCount,paperId"
}
headers = {
    "x-api-key": "TdLDusDP7R4GV44SsqXBlaQ7XmalveCTnqPQfP78"
}

# Send the GET request
response = requests.get(url, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Connect to SQLite database (it will create the database file if it doesn't exist)
    conn = sqlite3.connect('research_articles.db')
    cursor = conn.cursor()

    # Create the Articles_API table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Articles_API (
        PaperID TEXT PRIMARY KEY,
        Title TEXT,
        Authors TEXT,
        Abstract TEXT,
        Year INTEGER,
        CitationCount INTEGER
    );
    ''')

    # Insert each paper's data into the Articles_API table
    for paper in data.get('data', []):
        paper_id = paper.get('paperId')
        title = paper.get('title')
        authors = ', '.join([author['name'] for author in paper.get('authors', [])])
        abstract = paper.get('abstract')
        year = paper.get('year')
        citation_count = paper.get('citationCount')

        # Insert data into the table
        cursor.execute('''
        INSERT OR REPLACE INTO Articles_API (PaperID, Title, Authors, Abstract, Year, CitationCount)
        VALUES (?, ?, ?, ?, ?, ?);
        ''', (paper_id, title, authors, abstract, year, citation_count))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Data successfully fetched and stored in the database.")
else:
    print(f"Failed to fetch data: {response.status_code}")
