import requests

# GET AVALIAÇÕES

avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/')

print(avaliacao.json())
