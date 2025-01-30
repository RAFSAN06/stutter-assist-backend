from flask import Flask, request, send_file
from flask_cors import CORS
import librosa
import soundfile as sf
import numpy as np
import io

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_audio():
    audio_file = request.files['audio']
    audio, sr = librosa.load(audio_file, sr=16000)
    
    # Simulate processing: remove silence (placeholder)
    processed_audio, _ = librosa.effects.trim(audio, top_db=20)
    
    buffer = io.BytesIO()
    sf.write(buffer, processed_audio, sr, format='WAV')
    buffer.seek(0)
    return send_file(buffer, mimetype='audio/wav')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)