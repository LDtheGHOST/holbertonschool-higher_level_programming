# Utiliser l'image PostgreSQL officielle comme base
FROM postgres:latest

# Configuration des variables d'environnement pour initialiser la base de données
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

# Exposer le port par défaut utilisé par PostgreSQL (5432)
EXPOSE 5432

# Commande par défaut à exécuter lorsque le conteneur démarre
CMD ["postgres"]
