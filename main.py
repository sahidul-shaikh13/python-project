import gradio as gr
from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound
import os

# Function to convert text to speech using gTTS
def text_to_speech(text, lang='en', download=False):
    try:
        tts = gTTS(text=text, lang=lang)
        temp_file = NamedTemporaryFile(delete=False, suffix='.mp3')
        tts.save(temp_file.name)
        if download:
            return temp_file.name
        else:
            playsound(temp_file.name)
            os.remove(temp_file.name)
            return "Speech Generated Successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

# Define Gradio interface
iface = gr.Interface(
    fn=text_to_speech,
    inputs=[gr.components.Textbox(label="Enter text to convert to speech"),
            gr.components.Radio(["en", "es", "fr"], label="Language"),
            gr.components.Checkbox(label="Download Speech",)],
    outputs=gr.components.Textbox(label="Status"),
    title="Text-to-Speech",
    description="Convert text to speech using gTTS (Google Text-to-Speech)",
    theme="default"
)

# Launch the interface
iface.launch()
