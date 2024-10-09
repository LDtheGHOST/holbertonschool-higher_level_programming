# task_02_requests.py
import requests
import csv

def fetch_and_print_posts():
    """Récupère les publications de JSONPlaceholder et imprime les titres."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # Imprimer le status code
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        # Analyser les données JSON (java script objet notation) data
        posts = response.json()
        
        # Imprimer les titles
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """Récupère les publications de JSONPlaceholder les enregistre dans un fichier  CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Analyser les données JSON (java script objet notation) data
        posts = response.json()
        
        # Préparer les données pour data pour CSV
        data_to_write = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Écrire les données dans un fichier CSV
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data_to_write)
