DROP VIEW IF EXISTS cup_full_stats;
CREATE OR REPLACE VIEW cup_full_stats as (

SELECT 
p.player_id,
p.first_name,
c.course_name,
r.round_id,
r.round_date,
hs.hole_number,
coalesce(hs.par_yellow,hs.par_white) as par,
coalesce(hs.yards_yellow,hs.yards_white) as yards,
hs.stroke_index,
s.score 
from course c
JOIN hole_stats hs
ON c.course_id=hs.course_id
JOIN scores s
ON hs.hole_id=s.hole_id
JOIN round r
ON r.round_id=s.round_id
JOIN player p 
ON p.player_id=s.player_id
WHERE r.round_id in(46)
order by 1,4,5
);

--SELECT * FROM cup_full_stats;

DROP VIEW IF EXISTS cup_full_stats_hc;
CREATE OR REPLACE VIEW cup_full_stats_hc as (
SELECT *,
CASE 
WHEN player_id IN (5,6) THEN par+2
WHEN player_id=2 AND hole_number <=14 THEN par+2
WHEN player_id=2 AND hole_number >14 THEN par+1
WHEN player_id IN (3,4) AND stroke_index <=10 THEN par+2
WHEN player_id IN (3,4) AND stroke_index >10 THEN par+1
WHEN player_id IN (1,7) AND stroke_index <=8 THEN par+2
WHEN player_id IN (1,7) AND stroke_index >8 THEN par+1
WHEN player_id=8 THEN par+1
END AS par_adjusted
FROM cup_full_stats);


DROP VIEW IF EXISTS cup_full_stats_hcs;
CREATE OR REPLACE VIEW cup_full_stats_hcs as (
SELECT *,
score - par_adjusted as score_vs_adjusted
FROM cup_full_stats_hc);

SELECT * FROM cup_full_stats_hcs;