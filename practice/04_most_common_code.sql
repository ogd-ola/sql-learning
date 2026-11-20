/* Round 4: a preview of your project
What’s the most common code? This is the same pattern as your TTC “most common cause” question, just with codes instead of descriptions. */

select code, count(*) as num_occurrences
from delays
group by code 
order by num_occurrences desc
limit 1;

-- How many times does each code occur?
select code, count(*) as num_occurrences
from delays
group by code 
order by num_occurrences desc;
