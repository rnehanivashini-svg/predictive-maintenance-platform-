
import csv
from pathlib import Path
from backend.database import get_connection


CSV_PATH = next(
    (Path(__file__).resolve().parent.parent / "data").glob("*.csv")
)

print("Found CSV file:", CSV_PATH)


def import_data():
    records = []

    with open(CSV_PATH, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append((
                int(row["udi"]),
                row["product_id"],
                row["machine_type"],
                float(row["air_temperature"]),
                float(row["process_temperature"]),
                int(row["rotational_speed"]),
                float(row["torque"]),
                int(row["tool_wear"]),
                int(row["failure"])
            ))

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.executemany(
                """
                INSERT INTO public.machine_readings (
                    udi, product_id, machine_type,
                    air_temperature, process_temperature,
                    rotational_speed, torque, tool_wear,
                    failure
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (udi) DO NOTHING
                """,
                records
            )

            cursor.execute(
                "SELECT COUNT(*) AS total FROM public.machine_readings"
            )

            result = cursor.fetchone()
            print("Total records:", result["total"])

    print("Import completed successfully!")

if __name__ == "__main__":
    import_data()
