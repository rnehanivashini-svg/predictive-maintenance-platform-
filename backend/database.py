
import os
from pathlib import Path

import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

# Find your main project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Load Supabase connection details
load_dotenv(BASE_DIR / ".env")


def get_connection():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError("DATABASE_URL is missing from .env")

    return psycopg.connect(
        database_url,
        row_factory=dict_row,
        sslmode="require"
    )


if __name__ == "__main__":
    with get_connection() as connection:
        result = connection.execute(
            "SELECT COUNT(*) AS total FROM public.machine_readings"
        ).fetchone()

        print("Connected to Supabase!")
        print("Total machine records:", result["total"])
