# 🛡️ Cyber Log ETL Pipeline & Risk Analysis

**Author:** Sam Merrell
**Date:** 3/23/2026

---

## 📌 Project Overview

This project implements an end-to-end ETL pipeline to ingest, transform, and analyze cybersecurity network traffic logs. The pipeline converts raw log data into structured, queryable insights to help identify potentially malicious activity.

The goal is to simulate a real-world security analytics workflow by transforming raw data into a clean, relational format using Python and SQL.

---

## 🎯 Objectives

* Ingest raw network log data from CSV/Excel
* Clean and normalize data using Python (Pandas)
* Store structured data in PostgreSQL
* Analyze traffic patterns and identify high-risk IP behavior
* Generate insights using SQL queries

---

## 🧱 Architecture

```
Raw CSV/Excel → Python (Pandas) → Data Cleaning & Transformation → PostgreSQL → SQL Analysis
```

---

## 📂 Project Structure

```
Cyber-log-ETL/
│
├── data/
│   └── raw/                  # Original dataset (CSV/Excel)
│
├── src/
│   └── pipeline.py           # ETL pipeline (ingestion, transformation, loading)
│
├── sql/
│   ├── schema.sql            # Table creation script
│   └── analysis.sql          # SQL queries for insights
│
├── README.md
├── requirements.txt
```

---

## ⚙️ Technologies Used

* Python (Pandas)
* PostgreSQL
* SQL
* psycopg2
* DBeaver

---

## 🔄 Pipeline Workflow

```
Raw Data → Data Selection → Data Cleaning → Data Transformation → PostgreSQL Storage → SQL Analysis
```

---

## ⚙️ Pipeline Steps

### 1. Data Ingestion

* Loaded raw cybersecurity log data from CSV using Pandas
* Inspected dataset structure and column types

---

### 2. Data Selection

* Selected relevant fields:

  * timestamp
  * source/destination IPs
  * ports
  * URL
  * attack type

---

### 3. Data Transformation

* Renamed columns for consistency (e.g., `src_ip` → `source_ip`)
* Normalized categorical values (e.g., attack labels)
* Created derived field:

  * `is_malicious` (boolean classification of traffic)

---

### 4. Data Validation

* Verified schema alignment
* Checked for null values and data integrity
* Ensured proper data types (timestamp, numeric fields)

---

### 5. Data Storage

* Designed relational schema in PostgreSQL
* Created `network_events` table
* Inserted cleaned data using Python (`psycopg2`)

---

### 6. Data Analysis

* Wrote SQL queries to:

  * Identify top malicious source IPs
  * Analyze traffic distribution
  * Detect repeat offenders

---

## 📊 Example Query

```sql
-- Top malicious source IPs
SELECT source_ip, COUNT(*) AS malicious_count
FROM network_events
WHERE is_malicious = true
GROUP BY source_ip
ORDER BY malicious_count DESC
LIMIT 10;
```

---

## 🧠 Key Learnings

* Built an end-to-end ETL pipeline from raw data to database
* Applied data cleaning and normalization techniques
* Designed a relational schema for log-based data
* Used SQL to extract meaningful insights from structured data

---

## 🚀 Future Improvements

* Automate pipeline execution (scheduled runs)
* Add logging and error handling
* Optimize bulk data inserts
* Build a dashboard (Power BI / Tableau)

---

## 📌 Summary

This project demonstrates the full lifecycle of a data pipeline, from ingestion and transformation to storage and analysis, using real-world cybersecurity data.
