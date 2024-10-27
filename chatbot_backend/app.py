from flask import Flask, request, jsonify
from lib.azure_api import ApiAzure  # Importa la classe definita in azure_api.py

app = Flask(__name__)

# Inizializza una sola istanza della classe `api_azure`
azure_client = ApiAzure()

@app.route('/getPromptContent', methods=['POST'])
def getPromptContent():
    # Recupera il testo dalla richiesta
    content = request.json.get("content")
    
    try:
        # Usa il metodo `api_call` della classe `api_azure` per inviare la richiesta
        response = azure_client.prompt_call(content=content)
        
        # Restituisci la risposta JSON dal completamento dell'API di Azure OpenAI
        return jsonify(response)
    
    except Exception as e:
        # Gestisce eventuali errori nella richiesta
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000)
