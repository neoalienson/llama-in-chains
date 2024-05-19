import gradio as gr
from config import config
import data
import ui

def model_changed(input):
    print("B")    
    return gr.Dropdown(label="Model", choices=data.models, value=input)

with gr.Blocks() as parameters:
    with gr.Column():
        ui.mi_models = gr.Dropdown(label="Model")
        with gr.Accordion("Model Details"):
            ui.mi_model_details = gr.Markdown(label="Model Details")
        with gr.Accordion("Model File"):           
            ui.mi_modelfile = gr.Markdown(label="Model File")
        with gr.Accordion("Template"):
            ui.mi_template = gr.Markdown(label="Template")
        with gr.Accordion("Parameters"):
            ui.mi_parameters = gr.Markdown(label="Parameters")

