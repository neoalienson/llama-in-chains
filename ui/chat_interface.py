import gradio as gr
from config import config
import data.prompts as prompts
import ollama
import shared

def new_prompt_template(choice, tb):
    return choice

def run(prompt, history = None):
    messages = []
    if history:
        for u, a in history:
            messages.append({"role": "user", "content": u})
            messages.append({"role": "assistant", "content": a})
    messages.append({"role": "user", "content": prompt})
    
    response = ollama.chat(model=shared.selected_model, messages=messages, stream=False)
    return response['message']['content']

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
                fn=run,
                textbox=textbox,
                chatbot=chatbot,
            )
    return chatinterface