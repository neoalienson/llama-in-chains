import gradio as gr
from config import config
import data.prompts as prompts
import ollama_lib

def new_prompt_template(choice, tb):
    return gr.Textbox(value=choice, autofocus=True, autoscroll=True)


def create_chatinterface():
    textbox = gr.Textbox(elem_id="input_box", lines=3, min_width=800)
    chatbot = gr.Chatbot(show_copy_button=True, layout="panel")
    with gr.Blocks() as chatinterface:
        with gr.Row():
            quick_prompt = gr.Radio(
                prompts.prompt_list, label="Quick Prompt", info="Overwrite input with a template"
            )
            quick_prompt.change(new_prompt_template, [quick_prompt, textbox], textbox)
        
        with gr.Column():
            gr.ChatInterface(
                fn=ollama_lib.generate_chat_response,
                textbox=textbox,
                chatbot=chatbot,
            )
    return chatinterface