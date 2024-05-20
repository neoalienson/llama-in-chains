import gradio as gr
import json
from config import config
import ui.model_info
import ui.game
import ui.dropdown_models
import ui.chat_interface
from config import config
import ollama_lib
import data
import shared

def load_data():
    data.models = ollama_lib.list_models()
    selected = None
    if config.default_model:
        selected = config.default_model
    
    shared.selected_model = selected

    return gr.Dropdown(label="Model", choices=data.models, value=selected)

(model_info, model_details, model_file, model_template, model_parameters) = ui.model_info.create_model_info()
ci = ui.chat_interface.create_chatinterface()
game = ui.game.create_game()

with gr.Blocks() as demo:
    with gr.Row():
        gr.TabbedInterface([ci, model_info, game], ["Chat", "Model details", "Game"])
    model_list = ui.dropdown_models.create_models(model_details, model_file, model_template, model_parameters)
    demo.load(fn=load_data, outputs=model_list)

if __name__ == "__main__":
    demo.launch(server_name=config.gradio_server_name, server_port=int(config.gradio_server_port),blocked_paths=config.blocked_paths)
