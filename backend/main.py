
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from backend.database import get_connection

app = FastAPI(title="Predictive Maintenance API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/readings")
def get_readings(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT * FROM public.machine_readings
            ORDER BY udi
            LIMIT %s OFFSET %s
            """,
            (limit, offset)
        ).fetchall()

    return {
        "count": len(rows),
        "readings": rows
    }


@app.get("/api/summary")
def get_summary():
    with get_connection() as connection:
        result = connection.execute(
            """
            SELECT
                COUNT(*) AS total_records,
                COALESCE(SUM(failure), 0) AS failure_count
            FROM public.machine_readings
            """
        ).fetchone()

    return result
