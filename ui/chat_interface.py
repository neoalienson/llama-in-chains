import json
import gradio as gr
from config import config
import ui.parameters
import data.prompts as prompts
import ollama_lib
import data

def new_prompt_template(choice, tb):
    return gr.Textbox(value=choice, autofocus=True, autoscroll=True)

def model_changed(input):
    return gr.Dropdown(label="Model", choices=data.models, value=input)


textbox = gr.Textbox(elem_id="input_box", lines=3, min_width=800)
chatbot = gr.Chatbot(show_copy_button=True, layout="panel")
global ci_models

with gr.Blocks() as chat_interface:
    with gr.Row():
        ci_models = gr.Dropdown(label="Model")
        # select the first item as default model
        ci_models.select(fn=model_changed, inputs=ci_models, outputs=ui.parameters.pa_models)
        ci_models.value = "llama3:instruct"
        
        quick_prompt = gr.Radio(
            prompts.prompt_list, label="Quick Prompt", info="Overwrite input with a template"
        )
        quick_prompt.change(new_prompt_template, [quick_prompt, textbox], textbox)

    with gr.Column():
        chat = gr.ChatInterface(
            fn=ollama_lib.generate_chat_response,
            additional_inputs=[ci_models],
            textbox=textbox,
            chatbot=chatbot,
        )

