import requests

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
    # Iterate through the papers and display the required information
    for paper in data.get('data', []):
        print(f"Title: {paper.get('title')}")
        print(f"Authors: {', '.join([author['name'] for author in paper.get('authors', [])])}")
        print(f"Abstract: {paper.get('abstract')}")
        print(f"Year: {paper.get('year')}")
        print(f"Citation Count: {paper.get('citationCount')}")
        print(f"Paper ID: {paper.get('paperId')}")
        print("-" * 80)
else:
    print(f"Failed to fetch data: {response.status_code}")
