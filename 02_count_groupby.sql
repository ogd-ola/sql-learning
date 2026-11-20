/* Round 2: COUNT and GROUP BY
How many rows are in the table in total?
How many delays happened on each line?
How many delays happened at each station, with the busiest station first?
What’s the average delay in minutes per line?
What’s the total delay minutes per station?
*/

-- How many rows are in the table in total?
SELECT *, COUNT(*) AS num_delays
FROM delays;

-- How many delays happened on each line?
SELECT line, COUNT(*) as num_delays
FROM delays
GROUP BY line;

-- How many delays happened at each station, with the busiest station first?
SELECT station, COUNT(*) AS num_delays
from delays
group by station
order by Count(*) desc;

-- avg delay in minutes per line
SELECT line, AVG(delay_minutes) as avg_delay
from delays
group by line;

-- What’s the total delay minutes per station?
SELECT station, SUM(delay_minutes) AS total_delay
FROM delays
GROUP BY station;
