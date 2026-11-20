"""Load TTC subway delay data and delay code descriptions into SQLite.

Extract: read the two source CSV files.
Load:    rebuild the tables and insert every row.
Verify:  compare the number of rows read from each CSV with the number
         of rows in the matching table.

Source-to-target mapping (delays CSV -> subway_delays table):
    _id        -> id
    Date       -> delay_date
    Time       -> delay_time
    Day        -> day
    Station    -> station
    Code       -> code
    Min Delay  -> delay_minutes
    Min Gap    -> delay_gap_minutes
    Bound      -> bound
    Line       -> line
    Vehicle    -> vehicle

Codes CSV -> delay_codes table:
    _id         -> id
    CODE        -> code
    DESCRIPTION -> description
"""

import csv
import sqlite3

DB_PATH = "ttc_delays.db"
DELAYS_CSV = "data/TTC Subway Delay Data since 2025.csv"
CODES_CSV = "data/Code Descriptions.csv"

DELAYS_COLUMNS = 11
CODES_COLUMNS = 3

CREATE_DELAYS = """
CREATE TABLE subway_delays (
    id INTEGER PRIMARY KEY,
    delay_date TEXT,
    delay_time TEXT,
    day TEXT,
    station TEXT,
    code TEXT,
    delay_minutes INTEGER,
    delay_gap_minutes INTEGER,
    bound TEXT,
    line TEXT,
    vehicle INTEGER
)
"""

CREATE_CODES = """
CREATE TABLE delay_codes (
    id INTEGER,
    code TEXT PRIMARY KEY,
    description TEXT
)
"""

INSERT_DELAYS = """
INSERT INTO subway_delays (
    id, delay_date, delay_time, day, station, code,
    delay_minutes, delay_gap_minutes, bound, line, vehicle
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

INSERT_CODES = """
INSERT INTO delay_codes (id, code, description) VALUES (?, ?, ?)
"""


def to_int(value):
    """Convert a CSV string to an int, or None if it is blank."""
    value = value.strip()
    return int(value) if value else None


def to_text(value):
    """Return a stripped string, or None if it is blank."""
    value = value.strip()
    return value or None


def read_csv_rows(path, expected_columns):
    """Yield each data row of a CSV file as a list of strings.

    Skips the header and any blank lines. Raises ValueError if a row
    does not have the expected number of fields.
    """
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        next(reader)  # skip the header
        for row in reader:
            if not row:
                continue
            if len(row) != expected_columns:
                raise ValueError(
                    f"{path}, line {reader.line_num}: "
                    f"expected {expected_columns} fields, got {len(row)}"
                )
            yield row


def read_delays(path):
    """Read the delays CSV into a list of tuples matching INSERT_DELAYS."""
    return [
        (
            to_int(row[0]),   # id
            to_text(row[1]),  # delay_date
            to_text(row[2]),  # delay_time
            to_text(row[3]),  # day
            to_text(row[4]),  # station
            to_text(row[5]),  # code
            to_int(row[6]),   # delay_minutes
            to_int(row[7]),   # delay_gap_minutes
            to_text(row[8]),  # bound
            to_text(row[9]),  # line
            to_int(row[10]),  # vehicle
        )
        for row in read_csv_rows(path, DELAYS_COLUMNS)
    ]


def read_codes(path):
    """Read the codes CSV into a list of tuples matching INSERT_CODES."""
    return [
        (to_int(row[0]), to_text(row[1]), to_text(row[2]))
        for row in read_csv_rows(path, CODES_COLUMNS)
    ]


def create_tables(cur):
    """Drop and recreate both tables so every run starts clean."""
    cur.execute("DROP TABLE IF EXISTS subway_delays")
    cur.execute("DROP TABLE IF EXISTS delay_codes")
    cur.execute(CREATE_DELAYS)
    cur.execute(CREATE_CODES)


def count_rows(cur, table):
    """Return the number of rows in a table."""
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    return cur.fetchone()[0]


def report(cur, table, source_rows):
    """Print a CSV vs database row count comparison for one table."""
    db_rows = count_rows(cur, table)
    status = "OK" if db_rows == source_rows else "MISMATCH"
    print(f"{table}: CSV rows = {source_rows}, DB rows = {db_rows} [{status}]")


def main():
    # Extract
    delay_data = read_delays(DELAYS_CSV)
    code_data = read_codes(CODES_CSV)

    # Load
    con = sqlite3.connect(DB_PATH)
    try:
        cur = con.cursor()
        create_tables(cur)
        cur.executemany(INSERT_DELAYS, delay_data)
        cur.executemany(INSERT_CODES, code_data)
        con.commit()

        # Verify
        report(cur, "subway_delays", len(delay_data))
        report(cur, "delay_codes", len(code_data))
    finally:
        con.close()


if __name__ == "__main__":
    main()
