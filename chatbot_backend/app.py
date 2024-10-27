from flask import Flask, request, jsonify
from azure_api import api_azure  # Importa la classe definita in azure_api.py

app = Flask(__name__)

# Inizializza una sola istanza della classe `api_azure`
azure_client = api_azure()

@app.route('/send_text', methods=['POST'])
def send_text():
    # Recupera il testo dalla richiesta
    text = request.json.get("text")
    
    try:
        # Usa il metodo `api_call` della classe `api_azure` per inviare la richiesta
        response = azure_client.api_call(content=text)
        
        # Restituisci la risposta JSON dal completamento dell'API di Azure OpenAI
        return jsonify(response)
    
    except Exception as e:
        # Gestisce eventuali errori nella richiesta
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000)
