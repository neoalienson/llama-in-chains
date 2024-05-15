import gradio as gr
from config import config

with gr.Blocks() as parameters:
    with gr.Row():
        gr.Dropdown(label="Model")