class game:
    def __init__(self, begin, end):
        self.start = begin
        self.end = end


game_set = []
game_set.append(game(1, 3))
game_set.append(game(3, 4))
game_set.append(game(0, 7))
game_set.append(game(3, 8))
game_set.append(game(15, 19))
game_set.append(game(15, 20))
game_set.append(game(10, 15))
game_set.append(game(8, 18))
game_set.append(game(6, 12))
game_set.append(game(5, 10))
game_set.append(game(4, 14))
game_set.append(game(2, 9))


def maxGame(games):
    sorted_games = sorted(games, key=lambda x: x.end) 
    num = 0
    ren_end = sorted_games[0].end
    for i in range(1, len(sorted_games)-1):
        if(sorted_games[i].start >= ren_end):
            num += 1
            ren_end = sorted_games[i].end
    return num


print(maxGame(game_set))