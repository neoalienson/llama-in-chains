import gradio as gr
from config import config

def create_model_info():
    details = modelfile = template = parameters = None
    with gr.Blocks() as model_info:
        with gr.Column():
            with gr.Accordion("Model Details"):
                details = gr.Markdown(label="Model Details")
            with gr.Accordion("Model File"):           
                modelfile = gr.Markdown(label="Model File")
            with gr.Accordion("Template"):
                template = gr.Markdown(label="Template")
            with gr.Accordion("Parameters"):
                parameters = gr.Markdown(label="Parameters")
    return (model_info, details, modelfile, template, parameters) 
