
CREATE TABLE IF NOT EXISTS public.machine_readings (
    udi INTEGER PRIMARY KEY,
    product_id TEXT,
    machine_type TEXT,
    air_temperature DOUBLE PRECISION,
    process_temperature DOUBLE PRECISION,
    rotational_speed INTEGER,
    torque DOUBLE PRECISION,
    tool_wear INTEGER,
    failure INTEGER
);

ALTER TABLE public.machine_readings
ENABLE ROW LEVEL SECURITY;
