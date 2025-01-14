# Poetry Emotion Classification

🚀 **Poetry Emotion Classification** is a deep learning project aimed at categorizing poetry text into emotional states using advanced Natural Language Processing (NLP) techniques. This project leverages pre-trained transformer models, specifically **DistilRoBERTa**, to detect emotions in poetic compositions. 🌟

---

## Features

- **State-of-the-art NLP**: Utilizes a pre-trained transformer model (`j-hartmann/emotion-english-distilroberta-base`) for robust emotion classification.
- **Web Interface**: A user-friendly Flask-based web application for emotion analysis.
- **Real-time Analysis**: Quickly predicts the primary emotional state of poetry text.
- **Extensibility**: Easily adaptable for other text classification tasks.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Dataset](#dataset)
4. [Model](#model)
5. [Application](#application)
6. [Contributing](#contributing)
7. [License](#license)

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/poetry-emotion-classification.git
    cd poetry-emotion-classification
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the model weights (if necessary) and set up your environment.

---

## Usage

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000`.

3. Enter your poetry text in the provided input field to analyze its emotional state.

---

## Dataset

The project is designed to work with various poetry datasets. While it currently uses pre-trained models, you can fine-tune the model with custom datasets for better accuracy and domain-specific use cases. Suggested datasets:

- [Poetry Foundation Corpus](https://www.poetryfoundation.org/)
- [Emotion Dataset for NLP](https://huggingface.co/datasets/emotion)

---

## Model

This project uses the `j-hartmann/emotion-english-distilroberta-base` model from Hugging Face's Transformers library. The model is pre-trained for emotion classification tasks and supports the following emotions:

- Joy
- Sadness
- Anger
- Fear
- Surprise
- Love

---

## Application

The Flask web application accepts poetry text input and returns the primary detected emotion. Backend processing is powered by the Hugging Face Transformers pipeline.

### API Endpoint

- **URL:** `/analyze-emotion`
- **Method:** `POST`
- **Payload Example:**
    ```json
    {
        "text": "Your poetic verse here..."
    }
    ```
- **Response Example:**
    ```json
    {
        "emotion": "Joy"
    }
    ```

---

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add some feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---
