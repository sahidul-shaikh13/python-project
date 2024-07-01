import gradio as gr
from gtts import gTTS
from tempfile import NamedTemporaryFile
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Function to convert text to speech using gTTS
def text_to_speech(text, lang='en', download=False):
    try:
        tts = gTTS(text=text, lang=lang)
        temp_file = NamedTemporaryFile(delete=False, suffix='.mp3')
        tts.save(temp_file.name)
        temp_file.close()  # Close the file to release handle for other processes
        
        if download:
            return temp_file.name
        else:
            pygame.mixer.music.load(temp_file.name)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)
            pygame.mixer.music.stop()
            # os.remove(temp_file.name)
            return "Speech Generated Successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

# Define Gradio interface
iface = gr.Interface(
    fn=text_to_speech,
    inputs=[gr.components.Textbox(label="Enter text to convert to speech"),
            gr.components.Radio(["en", "es", "fr","hi"], label="Language"),
            gr.components.Checkbox(label="Download Speech",)],
    outputs=gr.components.Textbox(label="Status"),
    title="Text-to-Speech",
    description="Convert text to speech using gTTS (Google Text-to-Speech)",
    theme="default"
)

# Launch the interface
iface.launch()
