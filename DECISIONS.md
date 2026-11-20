# Project decisions

A running log of the choices I made on this project, what else I considered, and why. Dates are when I made the decision.

## 1. Dataset: TTC subway delay data (2025 onwards) + delay code descriptions
- **Date:** 2026-11-20
- **Alternatives considered:** Bike Share Toronto trips and stations
- **Why:** _General curiosity, as well as greater familiarity with the TTC, and thus more relevance_

## 2. Practice basic SELECT queries on a small made-up table before loading real data
- **Date:** 2026-11-20
- **Alternatives considered:** Going straight to loading the real CSV with Python
- **Why:** _To gain foundational experience first, in order to become properly versatile_

## 3. Write my own CREATE TABLE statements
- **Date:** 2026-11-20
- **Tables:** `subway_delays` (all 11 CSV columns, renamed to clean names such as `delay_minutes` and `delay_gap_minutes`) and `delay_codes` (`code` as primary key)
- **Alternatives considered:** Using `id` as the primary key of `delay_codes`; moving `vehicle` into its own table
- **Why:** _`code` is the common column between `delay_codes` and `subway_delays`, hence it makes sense to make `code` the primary key here, as the ids in `delay_codes` won't match those of `subway_delays`_

## 4. `load.py` drops and recreates both tables on every run
- **Date:** 2026-11-20
- **Alternatives considered:** `CREATE TABLE IF NOT EXISTS`
- **Why:** _prevents crashing the script due to duplicate tables in the database_

## 5. Plain `csv` + `sqlite3` for loading, no pandas
- **Date:** 2026-11-20
- **Alternatives considered:** pandas for loading and cleaning
- **Why:** _Although pandas is great for data cleaning, it also modifies data in a manner which can defeat the purpose of learning SQL in the first place_

---

## Template for new entries

## N. Short title of the decision
- **Date:**
- **Alternatives considered:**
- **Why:**
- **What happened afterwards (optional):** did it work out, would I change it?
