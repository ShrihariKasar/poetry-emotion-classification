from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize the emotion classifier
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze-emotion', methods=['POST'])
def analyze_emotion():
    data = request.get_json()
    poetry = data.get("text", "")
    if poetry:
        result = emotion_classifier(poetry)
        emotion = result[0]['label']  # Get the primary detected emotion
        return jsonify({"emotion": emotion})
    else:
        return jsonify({"error": "No text provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
