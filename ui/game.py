import gradio as gr
from config import config
import data
import ollama_lib
import data.games

def create_game():
    textbox = gr.Textbox(elem_id="input_box", lines=3, min_width=800)
    chatbot = gr.Chatbot(show_copy_button=True, layout="panel")    
    with gr.Blocks() as game:   
        with gr.Column():
            gr.ChatInterface(
                fn=ollama_lib.generate_chat_response,
                textbox=textbox,
                chatbot=chatbot,
            )

    return game