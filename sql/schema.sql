CREATE TABLE network_events (
    event_id SERIAL PRIMARY KEY,
    event_timestamp TIMESTAMP,
    source_ip TEXT,
    destination_ip TEXT,
    source_port INTEGER,
    destination_port INTEGER,
    url TEXT,
    attack_type TEXT
);