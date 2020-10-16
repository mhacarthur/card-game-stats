SELECT
    m.id AS match_id,
    m.date AS date,
    g.name AS game,
    p.name AS player,
    win.name as winner
FROM
     playermatch as pm
JOIN player AS p
    on p.id = pm.player
JOIN match AS m
    on m.id = pm.match
JOIN game AS g
    on g.id = m.game
JOIN (SELECT * FROM player) AS win
    on win.id = m.winner
;