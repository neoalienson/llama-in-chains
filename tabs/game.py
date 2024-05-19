import gradio as gr
from config import config
import data
import ui
import data.prompts as prompts

with gr.Blocks() as game:
    with gr.Column():
        gr.Dropdown(label="Model")
        