from gtts import gTTS
from flask 
from playsound import playsound
import tempfile
import os

# Function to create and play TTS audio
def speak(text, accent):
    # Select language based on accent
    lang = {
        "American": "en",       # 'en' defaults to US English in gTTS
        "British": "en-uk",     # UK English
        "Australian": "en-au"   # Australian English
    }.get(accent, "en")

    # Generate TTS audio
    tts = gTTS(text=text, lang=lang)
    
    # Save audio to a temporary file and then close it before playing
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_path = fp.name  # Get the file path

    tts.save(temp_path)  # Save TTS audio to the path
    playsound(temp_path)  # Play audio
    os.remove(temp_path)  # Delete temporary file after playback

# Example usage
sentence = input("Enter the sentence to pronounce: ")
accent = input("Choose accent (American, British, Australian): ")
speak(sentence, accent)
