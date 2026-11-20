/* Round 3: a stretch, using HAVING
Show only the stations that had more than 1 delay. */

SELECT station, COUNT(*) AS num_delays
from delays
group by station
HAVING count(*) > 1;
