# Utilisez une image Python officielle en tant qu'image de base
FROM python:3.9-slim-buster

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de l'application dans le conteneur
COPY . /app

# Installez les dépendances de l'application
RUN pip install --no-cache-dir -r requirements.txtre

# Exposez le port sur lequel l'application Flask écoute
EXPOSE 5016

# Définissez la commande à exécuter lorsque le conteneur démarre
CMD [ "python", "app.py" ]
