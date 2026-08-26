def criar_ranking(pontuacoes):
    ranking = sorted(pontuacoes, reverse=True)
    return ranking


pontuacoes = [50, 90, 70, 100, 80]

ranking = criar_ranking(pontuacoes)

print("Ranking de pontuação:", ranking)