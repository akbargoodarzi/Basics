from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    filename = 'speech.mp3'
    tts.save(filename)
    os.system(f"start {filename}")

# Usage
text = "Hello, welcome to the world of Python."
text_to_speech(text)
