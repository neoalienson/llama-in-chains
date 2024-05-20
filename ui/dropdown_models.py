import json
import gradio as gr
import ollama_lib
import shared

def model_changed(input):
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

    return [gr.Textbox(value=input, visible=False),
            gr.Markdown(label="Model Details", value=details),
            gr.Markdown(label="Model File", value=f"```\n{modelfile}\n```"),
            gr.Markdown(label="Template", value=f"```\n{template}\n```"),
            gr.Markdown(label="Model Parameterts", value=f"```\n{parameters}\n```"),
            ]

def create_models(model_details, model_file, model_template, model_parameters):
    with gr.Blocks():
        models = gr.Dropdown(label="Model", allow_custom_value=True)
        models.select(fn=model_changed, inputs=models, outputs=[
                shared.selected_model, model_details, model_file, model_template, model_parameters
            ])
    return models

