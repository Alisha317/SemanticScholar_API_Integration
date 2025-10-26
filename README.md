# SemanticScholar_API_Integration
Lab Project: Fetching research article metadata using Semantic Scholar API and SQL analytics
# Data Warehouse & BI Lab

## Objective
Integrate research article metadata from Semantic Scholar API into SQL database and perform analytical queries.

## Tasks Overview
### Task 1 – API Fetch
Fetch article metadata (title, authors, abstract, citations) using Python and Semantic Scholar API.  
**File:** `Task1_API_Fetch/task1_fetch.py`

### Task 2 – SQL Store
Create SQL table and store fetched articles.  
**File:** `Task2_SQL_Store/task2_store.py`

### Task 3 – Extend Metadata with References
Add references column and store cited papers.  
**File:** `Task3_Metadata_References/task3_references.py`

### Task 4 – Analytical Queries
Run SQL queries to find top-cited papers, authors, and yearly publication stats.  
**Files:** `Task4_Analytical_Queries/queries.sql` , `task4_analysis.py`

### Task 5 – Export to CSV
Export SQL table to CSV for further analysis.  
**File:** `Task5_CSV_Export/task5_export.py`

## Tools & Technologies
- Python (requests library)
- SQL (MySQL/SQLite)
- Semantic Scholar API
- CSV export

## How to Run
1. Clone repository  
2. Install Python dependencies: `pip install requests`  
3. Run Python scripts in order: Task1 → Task2 → Task3 → Task4 → Task5
