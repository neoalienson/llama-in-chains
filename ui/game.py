import gradio as gr
from config import config
import data
import data.prompts as prompts

def create_game():
    with gr.Blocks() as game:
        with gr.Column():
            gr.Dropdown(label="Model")

    return game