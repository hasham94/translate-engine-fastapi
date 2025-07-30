import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.schemas import VideoInput, SummaryInput
from services.downloader import download_audio
from services.transcriber import transcribe_audio
from services.translator import translate_text
from services.summarizer import simple_summarize

app = FastAPI()

# ✅ Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process")
async def process_video(data: VideoInput):
    try:
        audio_file = download_audio(data.url)
        transcribed_text = transcribe_audio(audio_file)
        # translated_text = translate_text(transcribed_text, data.target_language) in case open ai

        # I am using https://docs.libretranslate.com/ for free translation
        translated_text = ''
        if data.target_language != 'auto':
            translated_text = translate_text(transcribed_text, data.target_language)
        

        if os.path.exists(audio_file):
            os.remove(audio_file)

        return {
            "transcribed": transcribed_text,
            "translated": translated_text,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e.detail))

@app.post("/process/text")
async def process_text(data: SummaryInput):
    try:
        summary = simple_summarize(data.text)
        
        return {
            "summary": summary
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))