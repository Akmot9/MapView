from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2

# Définition du modèle de données pour les logs de connexion
class SignInLog(BaseModel):
    abuse: str
    address: str
    lat: str
    lng: str
    name: str
    threatintelname: str

# Initialisation de l'application FastAPI
app = FastAPI()

# Configuration du middleware CORS pour autoriser les requêtes cross-origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route pour récupérer les logs de connexion depuis la base de données
@app.get("/signin-logs")
def get_signin_logs():
    try:
        # Connexion à la base de données PostgreSQL
        conn = psycopg2.connect(
            host="your_database_host",
            port="your_database_port",
            dbname="your_database_name",
            user="your_database_user",
            password="your_database_password",
        )

        # Création d'un curseur pour exécuter des requêtes
        cur = conn.cursor()

        # Exécution de la requête SQL pour récupérer les logs de connexion
        cur.execute("SELECT * FROM signin_logs")

        # Récupération des résultats
        results = cur.fetchall()

        # Conversion des résultats en une liste de dictionnaires
        signin_logs = [
            {
                "abuse": result[0],
                "address": result[1],
                "lat": result[2],
                "lng": result[3],
                "name": result[4],
                "threatintelname": result[5],
            }
            for result in results
        ]

        # Fermeture du curseur et de la connexion à la base de données
        cur.close()
        conn.close()

        return signin_logs

    except (Exception, psycopg2.Error) as error:
        # Gestion des erreurs lors de la connexion à la base de données
        print("Error while connecting to PostgreSQL database:", error)
        return []

