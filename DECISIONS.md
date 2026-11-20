# Project decisions

A running log of the choices I made on this project, what else I considered, and why. Dates are when I made the decision.

## 1. Dataset: TTC subway delay data (2025 onwards) + delay code descriptions
- **Date:** 2026-11-20
- **Alternatives considered:** Bike Share Toronto trips and stations
- **Why:** _(your words: what made this the better pick?)_

## 2. Practice basic SELECT queries on a small made-up table before loading real data
- **Date:** 2026-11-20
- **Alternatives considered:** Going straight to loading the real CSV with Python
- **Why:** _(your words)_

## 3. Document the work as .sql files in a `practice` folder on GitHub, uploaded through the website
- **Date:** 2026-11-20
- **Alternatives considered:** GitHub Desktop (not available on the shared computer), OneDrive as the main store
- **Why:** _(your words)_

## 4. Write my own CREATE TABLE statements
- **Date:** 2026-11-20
- **Tables:** `subway_delays` (all 11 CSV columns, renamed to clean names such as `delay_minutes` and `delay_gap_minutes`) and `delay_codes` (`code` as primary key)
- **Alternatives considered:** Using `id` as the primary key of `delay_codes`; moving `vehicle` into its own table
- **Why:** _(your words: why `code` and not `id`? why keep `vehicle` as a plain column?)_

## 5. `load.py` drops and recreates both tables on every run
- **Date:** 2026-11-20
- **Alternatives considered:** `CREATE TABLE IF NOT EXISTS`
- **Why:** _(your words: what problem does this avoid when the script is re-run?)_

## 6. Plain `csv` + `sqlite3` for loading, no pandas
- **Date:** 2026-11-20
- **Alternatives considered:** pandas for loading and cleaning
- **Why:** _(your words)_

---

## Template for new entries

## N. Short title of the decision
- **Date:**
- **Alternatives considered:**
- **Why:**
- **What happened afterwards (optional):** did it work out, would I change it?
