from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa CORS
import os
import base64

app = Flask(__name__)
CORS(app)  # Abilita CORS per tutte le rotte

# Cartella per salvare i file caricati
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configura il percorso di salvataggio
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload/photo', methods=['POST'])
def upload_photo():
    data = request.get_json()  # Ottieni i dati dal body della richiesta

    if 'photo' not in data:
        return jsonify({"error": "No photo provided"}), 400

    # Estrai la stringa Base64
    base64_string = data['photo']
    # Rimuovi il prefisso "data:image/png;base64,"
    header, encoded = base64_string.split(',', 1)
    # Decodifica la stringa Base64
    binary_data = base64.b64decode(encoded)

    # Salva il file
    file_path = os.path.join(UPLOAD_FOLDER, 'uploaded_image.png')  # Specifica il percorso di salvataggio
    with open(file_path, 'wb') as file:
        file.write(binary_data)

    return jsonify({"message": "Photo uploaded successfully", "filename": 'uploaded_image.png'}), 201

@app.route('/upload/video', methods=['POST'])
def upload_video():
    data = request.get_json()  # Ottieni i dati dal body della richiesta
    if 'video' not in data:
        return jsonify({"error": "No video provided"}), 400

    # Estrai la stringa Base64
    base64_string = data['video']
    print(base64_string[:100])
    header, encoded = base64_string.split(',', 1)
    binary_data = base64.b64decode(encoded)

    video_path = os.path.join(UPLOAD_FOLDER, 'uploaded_video.mp4')
    with open(video_path, 'wb') as file:
        file.write(binary_data)

    return jsonify({"message": "Video uploaded successfully", "filename": 'uploaded_video.mp4'}), 201

if __name__ == '__main__':
    app.run(debug=True)
