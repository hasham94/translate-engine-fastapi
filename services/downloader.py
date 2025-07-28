import uuid
import yt_dlp
import os
import glob

def download_audio(url: str) -> str:
    base_filename = f"audio_{uuid.uuid4()}"
    output_template = f"{base_filename}.%(ext)s"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': '/opt/homebrew/bin',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    mp3_file = f"{base_filename}.mp3"
    if not os.path.exists(mp3_file):
        matches = glob.glob(f"{base_filename}*.mp3")
        if matches:
            return matches[0]
        else:
            raise FileNotFoundError(f"Audio file not found: {mp3_file}")

    return mp3_file
