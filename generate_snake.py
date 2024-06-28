import requests
import datetime

def fetch_contributions(username):
    url = f'https://github.com/users/{username}/contributions'
    response = requests.get(url)
    # Aqui você pode processar a resposta da API do GitHub para obter as contribuições
    # e gerar a imagem de "cobrinha"
    return response.text  # Exemplo simples, você precisa implementar o processamento correto

def main():
    username = 'DayvisonTi'
    contributions = fetch_contributions(username)
    print(contributions)  # Aqui você poderia gerar a imagem de "cobrinha"

if __name__ == '__main__':
    main()
