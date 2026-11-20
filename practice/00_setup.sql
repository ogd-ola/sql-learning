CREATE TABLE delays (
    id INTEGER PRIMARY KEY,
    delay_date TEXT,
    delay_time TEXT,
    day TEXT,
    station TEXT,
    line TEXT,
    code TEXT,
    delay_minutes INTEGER
);

INSERT INTO delays (delay_date, delay_time, day, station, line, code, delay_minutes) VALUES
('2025-10-01', '08:15', 'Wednesday', 'UNION STATION', 'YU', 'MUIS', 4),
('2025-10-01', '17:40', 'Wednesday', 'KENNEDY STATION', 'BD', 'TUSC', 0),
('2025-10-02', '09:05', 'Thursday', 'FINCH STATION', 'YU', 'SUDP', 7),
('2025-10-03', '18:20', 'Friday', 'UNION STATION', 'YU', 'PUOPO', 12),
('2025-10-04', '12:30', 'Saturday', 'BLOOR STATION', 'BD', 'MUIS', 3),
('2025-10-06', '07:50', 'Monday', 'KIPLING STATION', 'BD', 'TUSC', 5),
('2025-10-06', '08:45', 'Monday', 'UNION STATION', 'YU', 'SUDP', 9),
('2025-11-03', '17:10', 'Monday', 'FINCH STATION', 'YU', 'MUIS', 2),
('2025-11-05', '22:15', 'Wednesday', 'KENNEDY STATION', 'BD', 'PUOPO', 15),
('2025-11-07', '08:20', 'Friday', 'UNION STATION', 'YU', 'MUIS', 6),
('2025-12-01', '16:55', 'Monday', 'BLOOR STATION', 'BD', 'SUDP', 8),
('2025-12-02', '08:05', 'Tuesday', 'FINCH STATION', 'YU', 'TUSC', 0);
