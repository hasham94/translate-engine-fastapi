## Installation Guide

python -m venv venv
source venv/bin/activate 

## Run Script
uvicorn main:app --reload

## Install Required Libraries
pip install fastapi uvicorn pydantic yt-dlp openai python-dotenv
pip install git+https://github.com/openai/whisper.git
pip install ffmpeg-python


## Setup LibreTranslate Locally
pip install libretranslate
libretranslate
curl -X POST http://localhost:5000/translate -d q="Hello" -d source=en -d target=es