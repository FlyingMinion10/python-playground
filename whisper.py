from openai import OpenAI
client = OpenAI(api_key='YOUR_API_KEY')

audio_file = open("assets/Yssm meeting/P1.m4a", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
)

# Print the transcription
print(transcription.text)

# Download the transcription
transcription.download("transcription.txt")