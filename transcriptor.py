import moviepy.editor as mp
import speech_recognition as sr

def extract_audio_from_video(video_file, audio_file):
    # Cargar el video y extraer el audio
    video = mp.VideoFileClip(video_file)
    video.audio.write_audiofile(audio_file)

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        # Usar el reconocedor para transcribir el audio
        text = recognizer.recognize_google(audio, language='es-ES')
        print("Transcripción: " + text)
        return text
    except sr.UnknownValueError:
        print("El audio no se pudo entender.")
        return ""
    except sr.RequestError:
        print("No se pudo obtener resultados del servicio de reconocimiento.")
        return ""

def main():
    video_file = "/video.mp4"  # Reemplaza con la ruta de tu archivo de video
    audio_file = "audio.wav"          # Archivo temporal de audio

    extract_audio_from_video(video_file, audio_file)
    transcribe_audio(audio_file)

main()
