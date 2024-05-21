import json
import gradio as gr
import ollama_lib
import shared

def model_changed(input):
    shared.selected_model = input
    
    response = ollama_lib.model_details(input)
    details = json.dumps(response, indent=4, separators=(',', ': '))
    details = f"```\n{details}\n```"

    modelfile = ''
    parameters = ''
    template = ''
    
    if 'modelfile' in response:
        modelfile = response['modelfile']
    if 'parameters' in parameters:
        parameters = response['parameters']
    if 'template' in template:        
        template = response['template']

    return [
            details,
            f"```\n{modelfile}\n```",
            f"```\n{template}\n```",
            f"```\n{parameters}\n```",
            ]

def create_models(model_details, model_file, model_template, model_parameters):
    with gr.Blocks():
        models = gr.Dropdown(label="Model", allow_custom_value=True)
        models.select(fn=model_changed, inputs=models, outputs=[
                model_details, model_file, model_template, model_parameters
            ])
    return models

