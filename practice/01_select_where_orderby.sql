-- A few reminders:

-- Clause order is SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT.
-- WHERE filters rows. HAVING filters groups.
-- Text values go in single quotes, like 'YU'.

-- Ok, Now want to:
-- Show only the station and delay_minutes columns.
-- Show all delays on the YU line.
-- Show delays longer than 5 minutes, sorted from longest to shortest.
-- Show only the 3 longest delays.
-- Show delays on the BD line that were longer than 3 minutes.

-- SELECT * FROM delays 

SELECT station, delay_minutes
FROM delays;

SELECT * 
FROM delays
WHERE line = 'YU';

SELECT *
FROM delays
WHERE delay_minutes > 5
ORDER BY delay_minutes DESC;

select *
from delays
ORDER BY delay_minutes DESC
limit 3;

SELECT *
FROM delays
WHERE line = 'BD' and delay_minutes > 3;
