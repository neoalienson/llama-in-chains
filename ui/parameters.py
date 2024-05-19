import gradio as gr
from config import config

global pa_model_details
global pa_models

with gr.Blocks() as parameters:
    with gr.Row():
        pa_models = gr.Dropdown(label="Model")
        pa_model_details = gr.TextArea(info='Model Details')