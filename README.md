# Emotion Detector

An AI-based web application that detects emotions (anger, disgust, fear, joy,
and sadness) from a given piece of text, using the IBM Watson NLP library and
the Flask web framework.

## Features

- Detects five emotions: anger, disgust, fear, joy, sadness
- Returns the dominant emotion for a given statement
- Simple web interface built with Flask
- Includes error handling for blank/invalid input
- Unit tested with Python's `unittest`

## Project structure

- `EmotionDetection/emotion_detection.py` — core emotion detection logic
- `server.py` — Flask web server and routes
- `templates/index.html` — front-end page
- `test_emotion_detection.py` — unit tests

## Running locally

```bash
pip install -r requirements.txt
python server.py
```

Then visit `http://localhost:5000` in your browser.
