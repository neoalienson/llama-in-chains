import json
import gradio as gr
from config import config
import data.prompts as prompts
import ollama_lib
import data
import ui

def new_prompt_template(choice, tb):
    return gr.Textbox(value=choice, autofocus=True, autoscroll=True)

def model_changed(input):
    print(f"A:{input}")
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

    return [gr.Dropdown(label="Model", choices=data.models, value=input), 
            gr.Markdown(label="Model Details", value=details),
            gr.Markdown(label="Model File", value=f"```\n{modelfile}\n```"),
            gr.Markdown(label="Template", value=f"```\n{template}\n```"),
            gr.Markdown(label="Model Parameterts", value=f"```\n{parameters}\n```"),
            ]


textbox = gr.Textbox(elem_id="input_box", lines=3, min_width=800)
chatbot = gr.Chatbot(show_copy_button=True, layout="panel")

with gr.Blocks() as chat_interface:
    with gr.Row():
        ui.ci_models = gr.Dropdown(label="Model")
        # select the first item as default model
        ui.ci_models.value = "llama3:instruct"
        ui.ci_models.select(fn=model_changed, inputs=ui.ci_models, outputs=[
            ui.mi_models,
            ui.mi_model_details,
            ui.mi_modelfile,
            ui.mi_template,
            ui.mi_parameters
            ])

        quick_prompt = gr.Radio(
            prompts.prompt_list, label="Quick Prompt", info="Overwrite input with a template"
        )
        quick_prompt.change(new_prompt_template, [quick_prompt, textbox], textbox)

    with gr.Column():
        chat = gr.ChatInterface(
            fn=ollama_lib.generate_chat_response,
            additional_inputs=[ui.ci_models],
            textbox=textbox,
            chatbot=chatbot,
        )

