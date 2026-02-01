# Snowflake OpenWeather ELT Pipeline

This project demonstrates an **end-to-end ELT (Extract → Load → Transform) pipeline** built entirely in Snowflake using **OpenWeather API** data. It is designed to showcase modern data engineering practices, including semi-structured data ingestion, incremental transformations, and cost-efficient cloud warehousing.

---

## Purpose

The goal of this project is to demonstrate how to:

- Load raw JSON data from external APIs into Snowflake
- Build a **RAW → SILVER → GOLD layered architecture** for analytics
- Apply transformations **inside Snowflake** (ELT) rather than outside (ETL)
- Use **streams and tasks** to support incremental processing
- Optimize compute costs using Snowflake features such as auto-suspend warehouses
- Provide a reproducible, version-controlled project structure

---

## Architecture
- Data source: OpenWeather API (JSON)
- Storage & compute: Snowflake
- Layers: RAW → SILVER → GOLD
- Orchestration: Snowflake Streams & Tasks
- Transformations: Snowflake SQL (no dbt)

---

## Key Snowflake Features Used
- Stages & COPY INTO
- VARIANT data types
- Streams & Tasks
- Incremental MERGE logic
- Window functions & QUALIFY
- Cost-aware warehouse configuration


