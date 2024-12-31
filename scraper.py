import requests
from bs4 import BeautifulSoup
import json
import os

# Função para raspar as notícias
def scrape_bbc():
    url = 'https://www.bbc.com/news'  # URL da página de notícias da BBC
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []

    # Encontrar os links completos para os artigos
    for article in soup.find_all('a', href=True):
        link = article['href']
        
        # Verifica se o link é do formato desejado
        if link.startswith('/news/articles/'):
            # Completa o link com a URL base
            full_link = f'https://www.bbc.com{link}'
            
            # Pega o título do artigo
            title = article.get_text(strip=True)
            if title:
                articles.append({'title': title, 'link': full_link})

    return articles

# Caminho do arquivo JSON
json_file = 'data/news.json'

# Verificar se o arquivo JSON já existe
if os.path.exists(json_file):
    # Se o arquivo já existir, carregar os dados antigos
    with open(json_file, 'r', encoding='utf-8') as f:
        existing_articles = json.load(f)
else:
    existing_articles = []

# Raspar as notícias da BBC
new_articles = scrape_bbc()

# Adicionar as novas notícias à lista existente
existing_articles.extend(new_articles)

# Salvar os dados atualizados no arquivo JSON
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(existing_articles, f, ensure_ascii=False, indent=4)

print(f"Scraper completed! {len(new_articles)} articles saved.")
