import requests
import sqlite3
import json

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

# Function to fetch references for a given paper
def fetch_references(paper_id):
    ref_url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/references"
    response = requests.post(ref_url, headers=headers)
    if response.status_code == 200:
        references = response.json().get('data', [])
        # Extract at least 2 references
        return [{'paperId': ref.get('paperId'), 'title': ref.get('title')} for ref in references[:2]]
    else:
        print(f"Failed to fetch references for {paper_id}: {response.status_code}")
        return []

# Connect to SQLite database
conn = sqlite3.connect('research_articles.db')
cursor = conn.cursor()

# Add Reference_List column if it doesn't exist
cursor.execute('''
ALTER TABLE Articles_API
ADD COLUMN Reference_List TEXT;
''')

# Send the GET request to fetch papers
response = requests.get(url, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Insert each paper's data into the Articles_API table
    for paper in data.get('data', []):
        paper_id = paper.get('paperId')
        title = paper.get('title')
        authors = ', '.join([author['name'] for author in paper.get('authors', [])])
        abstract = paper.get('abstract')
        year = paper.get('year')
        citation_count = paper.get('citationCount')

        # Fetch references for the paper
        references = fetch_references(paper_id)
        references_json = json.dumps(references)

        # Insert data into the table
        cursor.execute('''
        INSERT OR REPLACE INTO Articles_API (PaperID, Title, Authors, Abstract, Year, CitationCount, Reference_List)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        ''', (paper_id, title, authors, abstract, year, citation_count, references_json))

    # Commit changes and close the connection
    conn.commit()
    print("Data successfully fetched and stored in the database.")
else:
    print(f"Failed to fetch data: {response.status_code}")

# Close the database connection
conn.close()
