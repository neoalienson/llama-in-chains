import json
import gradio as gr
from config import config
import ui.parameters
import data.prompts as prompts
import ollama_lib
import data.models as models

def new_prompt_template(choice, tb):
    return gr.Textbox(value=choice, autofocus=True, autoscroll=True)


textbox = gr.Textbox(elem_id="input_box", lines=3, min_width=800)
chatbot = gr.Chatbot(show_copy_button=True, layout="panel")

with gr.Blocks() as chat_interface:
    with gr.Row():
        dropdown = gr.Dropdown(label="Model", choices=models.models)
        # select the first item as default model
        dropdown.value = "llama3:instruct"

        quick_prompt = gr.Radio(
            prompts.prompt_list, label="Quick Prompt", info="Overwrite input with a template"
        )
        quick_prompt.change(new_prompt_template, [quick_prompt, textbox], textbox)

    with gr.Column():
        chat = gr.ChatInterface(
            fn=ollama_lib.generate_chat_response,
            additional_inputs=[dropdown],
            textbox=textbox,
            chatbot=chatbot,
        )

