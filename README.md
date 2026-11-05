# predictive-maintenance-platform-
DS_project


# IoT Predictive Maintenance Platform

## Project Overview

This project is an IoT Predictive Maintenance Platform
designed to store, retrieve, and analyze machine sensor data.

The backend uses FastAPI and Supabase PostgreSQL to
manage 10,000 machine readings.

The goal is to help identify patterns in machine
performance and support predictive maintenance.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Supabase (PostgreSQL)
- Psycopg
- Python-dotenv
- Visual Studio Code

## Project Structure

predictive-maintenance-platform-/
├── backend/
│   ├── __init__.py
│   ├── database.py
│   ├── import_data.py
│   ├── main.py
│   └── schema.sql
├── data/
│   └── machine_data.csv
├── .env
├── .gitignore
├── requirements.txt
└── README.md

## Database

Database: Supabase PostgreSQL

Table: machine_readings

Primary Key: udi

Columns:
- udi
- product_id
- machine_type
- air_temperature
- process_temperature
- rotational_speed
- torque
- tool_wear
- failure

Total Records: 10,000

The CSV importer uses ON CONFLICT (udi) DO NOTHING
to prevent duplicate records.

## Installation and Setup

### 1. Clone the Repository

git clone YOUR_REPOSITORY_URL

cd predictive-maintenance-platform-

### 2. Create a Virtual Environment

On Mac:

python3 -m venv .venv

source .venv/bin/activate

On Windows:

python -m venv .venv

.venv\Scripts\activate

### 3. Install Dependencies

python -m pip install -r requirements.txt

### 4. Configure Supabase

Create a .env file in the main project folder.

Add your Supabase PostgreSQL connection string:

DATABASE_URL=YOUR_SUPABASE_CONNECTION_STRING

Use the complete session pooler connection string
from the Supabase dashboard.

Replace the password placeholder with your actual
database password.

Do not share or commit the .env file.

### 5. Set Up the Database

Open the Supabase SQL Editor.

Run the SQL commands in backend/schema.sql
to create the machine_readings table.

If your team's database has already been set up,
you can skip this step.

### 6. Import Machine Data

Place the cleaned machine dataset CSV in the
data folder.

Ensure the filename matches the path expected
by backend/import_data.py.

Run:

python -m backend.import_data

The script imports records and avoids duplicates.

### 7. Test the Database Connection

Run:

python -m backend.database

Expected output:

Connected to Supabase!
Total machine records: 10000

### 8. Start the FastAPI Server

Run:

python -m uvicorn backend.main:app --reload

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

### GET /health

Purpose:
Check whether the FastAPI server is running.

Example response:

{
  "status": "ok"
}

### GET /api/readings?limit=10

Purpose:
Retrieve machine sensor readings from Supabase.

Parameters:
- limit: number of records (1 to 100)
- offset: number of records to skip

Example request:

http://127.0.0.1:8000/api/readings?limit=10

Example response structure:

{
  "count": 1,
  "readings": [
    {
      "udi": 1,
      "product_id": "M14860",
      "machine_type": "M",
      "air_temperature": 298.1,
      "process_temperature": 308.6,
      "rotational_speed": 1551,
      "torque": 42.8,
      "tool_wear": 0,
      "failure": 0
    }
  ]
}

Note: This example illustrates the response format
for a request returning one record.

### GET /api/summary

Purpose:
Retrieve total machine records and failures.

Example response for the standard AI4I dataset:

{
  "total_records": 10000,
  "failure_count": 339
}

## API Testing

The endpoints can be tested using FastAPI Swagger UI:

http://127.0.0.1:8000/docs

Testing completed:
- GET /health returns HTTP 200
- GET /api/readings returns HTTP 200
- GET /api/summary returns HTTP 200
- Valid limits return HTTP 200
- Invalid limits return HTTP 422

Examples of invalid limits:
- limit=0
- limit=-5
- limit=10000

## Data Flow

Original CSV Dataset
        |
        v
Supabase PostgreSQL Database
        |
        v
FastAPI Backend
        |
        v
Frontend Dashboard

## Frontend Integration

The frontend can communicate with FastAPI using:

GET /health

GET /api/readings?limit=10

GET /api/summary

Local backend address:

http://127.0.0.1:8000

The frontend must use a reachable backend address
when running on another computer or when deployed.

## Security

- Database credentials are stored in .env
- .env is excluded using .gitignore
- Database passwords must not be committed to GitHub
- Database access should remain on the backend

## Team Responsibilities

CIST Backend:
- Database schema
- CSV ingestion
- Supabase connection
- FastAPI endpoints
- API testing and documentation

Data Science:
- Data cleaning
- Exploratory data analysis
- Predictive modeling

Frontend:
- Dashboard interface
- API integration
- Machine data visualization
