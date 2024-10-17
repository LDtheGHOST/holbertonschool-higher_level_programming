#!/usr/bin/python3
import requests 
        """improte la bibiotheque requte"""

import csv
        """improte la bibiotheque csv """


def fetch_and_print_posts():
       """ la je cree ou defini une fonction """

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
        """ je fais une demande de requete pour avoir les posts du url"""

    print(f"Status Code: {response.status_code}")
        """Imprimer le status code"""

    if response.status_code == 200:
        # Analyser les données JSON (java script objet notation) data
        """je fais une condition sile status code est 200"""

        posts = response.json()
        """si la condition est bon on lenregitre dans posts avec json"""

        for post in posts:
            """dans la boucle je dis que posts est dans posts pour trouver tout ce que jai mis a json"""

            print(post['title'])
            """la on imprime le post"""



def fetch_and_save_posts():
       """ la je cree ou defini une fonction la meme fonction pour avoir la meme base"""

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
        """ la je fais les meme demarche que dans la premier partie"""

    print(f'Status Code: {response.status_code}')
        """j'imprimele status code"""

    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', mode='w', newline='') as file:
        """permet de tout mettre dans un fiher csv comme si c'etait un json avec lecrit w et eviter les sau de ligne """
        
        with open('posts.csv', 'w', newline='') as csvfile:
            """" on ouvre le ficherwith open pour erire dans le ficher csv"""

            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            for post in posts:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})
                """ cree un dictinnaire dans le ficher csv ou on va trouverles infos id, body, etc.. de chaque post"""