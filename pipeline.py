import pandas as pd
import psycopg2

#file path
file_path = r"C:\Users\Sam Merrell\Desktop\Coding\SQL Projects\Cyber-Log-ETL\data\raw\cybersecurity.csv"
#load data
df = pd.read_csv(file_path)

columns_to_keep = [
    "timestamp",
    "src_ip",
    "dst_ip",
    "src_port",
    "dst_port",
    "url",
    "attack_type"
]
df_clean = df[columns_to_keep].copy()
#rename columns to match database schema
df_clean = df_clean.rename(columns={
    "timestamp": "event_timestamp",
    "src_ip": "source_ip",
    "dst_ip": "destination_ip",
    "src_port": "source_port",
    "dst_port": "destination_port"
})
print(df_clean.columns)
# We are normalizing the data to avoid any issues with inconsistent formatting. This is especially important for the attack_type column, which may have variations in how attack types are labeled (e.g., "DDoS" vs "ddos"). By converting all attack labels to lowercase and stripping any extra whitespace, we can ensure that our analysis will be more accurate and that we won't have duplicate entries for the same attack type due to formatting differences.
# normalize attack labels
df_clean["attack_type"] = df_clean["attack_type"].astype(str).str.strip().str.lower()

# create boolean flag
df_clean["is_malicious"] = df_clean["attack_type"] != "benign"

# convert types
df_clean["event_timestamp"] = pd.to_datetime(df_clean["event_timestamp"], errors="coerce")
df_clean["source_port"] = pd.to_numeric(df_clean["source_port"], errors="coerce")
df_clean["destination_port"] = pd.to_numeric(df_clean["destination_port"], errors="coerce")

# validate
print(df_clean.head())
print(df_clean.info())
print(df_clean.isnull().sum())
print(df_clean["is_malicious"].value_counts())

#Connect to PostgreSQL database
import psycopg2
conn = psycopg2.connect(
    dbname="cyber_db",
    user="postgres",
    password="Bucharest1990!",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

for _, row in df_clean.iterrows():
    cur.execute("""
        INSERT INTO network_events (
            event_timestamp,
            source_ip,
            destination_ip,
            source_port,
            destination_port,
            url,
            attack_type,
            is_malicious
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row["event_timestamp"],
        row["source_ip"],
        row["destination_ip"],
        row["source_port"],
        row["destination_port"],
        row["url"],
        row["attack_type"],
        row["is_malicious"]
    ))

#Close connection to DB
conn.commit()
cur.close()
conn.close()

#inspect data
print(df_clean.head()) # this will read just the first 5 entries of the dataset.
print(df_clean.columns) # this will read the column names of the dataset.
print(df_clean.dtypes) # this will read the data types of each column in the dataset. This is important to understand the structure of the data and to identify any potential issues with data types that may need to be addressed during data cleaning and preprocessing.