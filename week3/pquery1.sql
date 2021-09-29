select t.name from (
select teams.name,count(*) from teams, matches where teams.team_id = matches.host_team_id group by teams.team_id
union
select teams.name,count(*) from teams, matches where teams.team_id = matches.guest_team_id group by teams.team_id) as t group by t.name having sum(count)>3