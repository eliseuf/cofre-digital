from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():

    ambiente = os.getenv("ENVIRONMENT", "desconhecido")
    senha = os.getenv("DB_PASSWORD", "não configurada")

    return {
        "ambiente": ambiente,
        "senha_configurada": senha != "não configurada"
    }

app.run(host="0.0.0.0", port=5000)
