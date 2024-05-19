import gradio as gr
from config import config
import data
import ui

def model_changed(input):
    print("B")    
    return gr.Dropdown(label="Model", choices=data.models, value=input)

with gr.Blocks() as parameters:
    with gr.Column():
        ui.pa_models = gr.Dropdown(label="Model")
#        ui.pa_models.select(fn=model_changed, inputs=ui.pa_models, outputs=ui.ci_models)
        with gr.Accordion("Model Details"):
            ui.pa_model_details = gr.Markdown(label="Model Details")
        with gr.Accordion("Model File"):           
            ui.pa_modelfile = gr.Markdown(label="Model File")
        with gr.Accordion("Template"):
            ui.pa_template = gr.Markdown(label="Template")
        with gr.Accordion("Parameters"):
            ui.pa_parameters = gr.Markdown(label="Parameters")

