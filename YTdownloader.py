from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_video_as_mp3(youtube_url, output_path='.'):
    # Descargar el video de YouTube
    video = YouTube(youtube_url)
    stream = video.streams.filter(only_audio=True).first()
    download_path = stream.download(output_path=output_path)
    
    # Convertir el archivo descargado a MP3
    base, ext = os.path.splitext(download_path)
    mp3_path = base + '.mp3'
    
    audio = AudioSegment.from_file(download_path)
    audio.export(mp3_path, format="mp3")
    
    # Eliminar el archivo de audio original si es necesario
    os.remove(download_path)
    
    print(f'Descargado y convertido: {mp3_path}')

# Ejemplo de uso
youtube_url = 'https://www.youtube.com/watch?v=AD6wqKo51MU'  # Reemplaza con el URL de YouTube
download_youtube_video_as_mp3(youtube_url)
