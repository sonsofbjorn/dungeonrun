# Highscore function
def get_top_highschores(n):
    scores = []
    filename = "players.txt"
    with open(filename, mode="r") as f:
        for line in f: scores.append(int(line.split(',')[-1]))
    scores.sort()
    scores.reverse()
    return scores[:n]

print(get_top_highschores(5))
