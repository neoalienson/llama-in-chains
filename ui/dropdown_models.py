import json
import gradio as gr
import ollama
import shared

def model_changed(input):
    shared.selected_model = input
    
    response = ollama.show(input)
    details = json.dumps(response, indent=4, separators=(',', ': '))

    details = f"```\n{details}\n```"

    modelfile = ''
    parameters = ''
    template = ''
    
    if 'modelfile' in response:
        modelfile = response['modelfile']
    if 'parameters' in response:
        parameters = response['parameters']
    if 'template' in response:        
        template = response['template']

    return [
            details,
            f"```\n{modelfile}\n```",
            f"```\n{template}\n```",
            f"```\n{parameters}\n```",
            ]

def create_models(model_details = None, model_file = None, model_template = None, model_parameters = None):
    with gr.Blocks():
        models = gr.Dropdown(allow_custom_value=True, interactive=True)
        if model_details:
            models.select(fn=model_changed, inputs=models, outputs=[
                    model_details, model_file, model_template, model_parameters
                ])
    return models

