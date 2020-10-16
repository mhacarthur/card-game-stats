games = [
    dict(date="26-9-20", game="Lhama", players=["David", "Arturo", "Isela"], winner="Isela"),
    dict(date="26-9-20", game="Lhama", players=["David", "Arturo", "Isela"], winner="Isela"),
    dict(date="26-9-20", game="Lhama", players=["David", "Arturo", "Isela"], winner="David"),
    dict(date="26-9-20", game="Lhama", players=["David", "Arturo", "Isela"], winner="David"),
    dict(date="26-9-20", game="Lhama", players=["David", "Arturo", "Isela"], winner="Arturo"),
    dict(date="26-9-20", game="Lhama", players=["David", "Arturo", "Isela"], winner="Isela"),
    
    dict(date="26-9-20", game="Port Royal", players=["David", "Arturo", "Isela"], winner="Isela"),
    dict(date="26-9-20", game="Port Royal", players=["David", "Arturo", "Isela"], winner="David"),
    dict(date="26-9-20", game="Port Royal", players=["David", "Arturo", "Isela"], winner="Arturo"),
    
    dict(date="26-9-20", game="Munchkin", players=["David", "Arturo", "Isela"], winner="Isela"),
    dict(date="26-9-20", game="Munchkin", players=["David", "Arturo", "Isela"], winner="Arturo"),
    dict(date="26-9-20", game="Munchkin", players=["David", "Arturo", "Isela"], winner="Arturo"),
    
    dict(date="26-9-20", game="Encantados", players=["David", "Arturo", "Isela"], winner="David"),
    dict(date="26-9-20", game="Encantados", players=["David", "Arturo", "Isela"], winner="Arturo"),
    
    dict(date="26-9-20", game="Saboteur", players=["David", "Arturo", "Isela"], winner="Arturo"),
    dict(date="26-9-20", game="Saboteur", players=["David", "Arturo", "Isela"], winner="Arturo"),
    
    dict(date="9-10-20", game="Lhama", players=["David", "Arturo", "Isela"], winner="David"),
    dict(date="9-10-20", game="Lhama", players=["David", "Arturo", "Isela"], winner="David"),
    dict(date="9-10-20", game="Lhama", players=["David", "Arturo", "Isela"], winner="David"),
    
    dict(date="9-10-20", game="Port Royal", players=["David", "Arturo", "Isela"], winner="David"),
    dict(date="9-10-20", game="Port Royal", players=["David", "Arturo", "Isela"], winner="Arturo"),
    dict(date="9-10-20", game="Port Royal", players=["David", "Arturo", "Isela"], winner="Arturo"),
    
    dict(date="9-10-20", game="Bohnanza", players=["David", "Arturo", "Isela"], winner="Isela"),
    
    dict(date="9-10-20", game="Encantados", players=["Adriano", "David", "Arturo", "Isela"], winner="Arturo"),
    
    dict(date="9-10-20", game="Lhama", players=["David", "Adriano", "Arturo", "Isela"], winner="David"),
    dict(date="9-10-20", game="Lhama", players=["David", "Adriano", "Arturo", "Isela"], winner="David"),
    
    dict(date="9-10-20", game="Ninja Camp", players=["David", "Adriano", "Arturo", "Isela"], winner="Arturo"),
    dict(date="9-10-20", game="Bohnanza", players=["David", "Adriano", "Arturo", "Isela"], winner="Arturo"),
    
    dict(date="9-10-20", game="Saboteur", players=["David", "Adriano", "Arturo", "Isela"], winner="Arturo"),
    
    dict(date="9-10-20", game="Munchkin", players=["David", "Adriano", "Arturo", "Isela"], winner="Isela"),
    
    dict(date="10-10-20", game="Lhama", players=["Arturo", "Adriano", "Isela"], winner="Adriano"),
    dict(date="10-10-20", game="Lhama", players=["Arturo", "Adriano", "Isela"], winner="Adriano"),
    dict(date="10-10-20", game="Lhama", players=["Arturo", "Adriano", "Isela"], winner="Arturo"),
    dict(date="10-10-20", game="Lhama", players=["Arturo", "Adriano", "Isela"], winner="Isela"),
    
    dict(date="10-10-20", game="Encantados", players=["Arturo", "Adriano", "Isela"], winner="Arturo"),
    
    dict(date="10-10-20", game="Port Royal", players=["Arturo", "Adriano", "Isela"], winner="Arturo"),
    dict(date="10-10-20", game="Port Royal", players=["Arturo", "Adriano", "Isela"], winner="Arturo"),
    
    dict(date="10-10-20", game="Bohnanza", players=["Arturo", "Adriano", "Isela"], winner="Isela"),
    dict(date="10-10-20", game="Bohnanza", players=["Arturo", "Adriano", "Isela"], winner="Isela"),
]

player_names = [
    'Adriano', 'Arturo', 'David', 'Isela'
]
game_names = ['Bohnanza', 'Encantados', 'Lhama', 'Munchkin', 
    'Ninja Camp', 'Port Royal', 'Saboteur'
]
player_names = {name: fk+1 for fk, name in enumerate(player_names)}
game_names = {name: fk+1 for fk, name in enumerate(game_names)}

for match, game in enumerate(games):
    d = "%s 00:00:00"%'-'.join(game['date'].split('-')[::-1])
    g = game_names[game['game']]
    w = player_names[game['winner']]
#     print("INSERT INTO Match (date, game, winner) VALUES (\'%s\', %s, %s);"%(d, g, w))
    for player in game['players']:
        p = player_names[player]
        print("INSERT INTO PlayerMatch (player, match) VALUES (%d, %d);"%(p, match+1))