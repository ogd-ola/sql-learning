# TTC Subway Delays: SQL Analysis Project

A small end-to-end SQL project: load TTC subway delay data into SQLite with Python, analyze it with SQL queries, and validate the data with quality checks.

> **Status:** data loading is done. Analysis queries, data quality checks, and tests are in progress.

## Dataset

- **Source:** [Toronto Open Data](https://open.toronto.ca), "TTC Subway Delay Data" and its delay code descriptions file
- **Downloaded:** November 20, 2026 (the TTC keeps adding rows to this running dataset, so the files here are a fixed snapshot)
- **Size:** 47,915 delay records (2025 onwards) and 140 delay codes
- **Licence:** _https://open.toronto.ca/open-data-licence/_

## Tables

**`subway_delays`** (one row per delay incident)

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER, primary key | |
| delay_date | TEXT | `YYYY-MM-DD` |
| delay_time | TEXT | `HH:MM` |
| day | TEXT | day of the week |
| station | TEXT | |
| code | TEXT | links to `delay_codes.code` |
| delay_minutes | INTEGER | |
| delay_gap_minutes | INTEGER | |
| bound | TEXT | direction; blank in the source becomes NULL |
| line | TEXT | |
| vehicle | INTEGER | |

**`delay_codes`** (one row per delay code)

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER | |
| code | TEXT, primary key | |
| description | TEXT | |

## Source-to-target mapping

| CSV file | CSV column | Table column |
|----------|-----------|--------------|
| TTC Subway Delay Data since 2025.csv | `_id` | `subway_delays.id` |
| | `Date` | `delay_date` |
| | `Time` | `delay_time` |
| | `Day` | `day` |
| | `Station` | `station` |
| | `Code` | `code` |
| | `Min Delay` | `delay_minutes` |
| | `Min Gap` | `delay_gap_minutes` |
| | `Bound` | `bound` |
| | `Line` | `line` |
| | `Vehicle` | `vehicle` |
| Code Descriptions.csv | `_id` | `delay_codes.id` |
| | `CODE` | `code` |
| | `DESCRIPTION` | `description` |

Blank values in the CSVs are loaded as NULL.

## Questions the queries answer

1. Which line had the most delays in 2025?
2. Which day of the week had the most delays?
3. Which month had the most delays in 2025?
4. Which hour of the day had the most delays in Q4 2025?
5. What is the average delay length per line?
6. Which stations had more than 100 delays?
7. What are the most common causes of delay, by description?
8. Which stations lost more total minutes than the average station?

## Data quality checks

_To be added: NULL counts per column, duplicate rows, out-of-range values, and CSV-to-database row count reconciliation, with what I found and what I did about it._

## Known limitations

- The data records only delays, not normal trips, so rates (for example, delays per train) cannot be computed without service or ridership data.
- Some records have a delay of 0 minutes; see the analysis notes for how these are treated.
- Incidents are logged by hand, so patterns can partly reflect how delays are recorded.

## How to run

Requires Python 3 (standard library only, no extra packages).

1. Put the two CSV files in the `data/` folder.
2. Run `python load.py` from the project root.
3. The script builds `ttc_delays.db` and prints a CSV vs database row count for each table.
4. Run the queries in `queries.sql` against `ttc_delays.db` with any SQLite tool.

## Project structure

```
├── README.md
├── DECISIONS.md      # choices I made and why
├── load.py           # CSV -> SQLite loader with row count check
├── data/             # source CSV files (snapshot)
└── practice/         # SQL practice queries
```
