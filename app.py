import gradio as gr
import json
from config import config
import ui.model_info
import ui.game
import ui.dropdown_models
import ui.chat_interface
from config import config
import data
import shared
import ollama

def load_data():
    response = ollama.list()

    data.models = [item['name'] for item in response['models']]
    selected = None
    if config.default_model:
        selected = config.default_model
    shared.selected_model = selected

    selected_embedding = None
    if config.default_embedding_model:
        selected_embedding = config.default_embedding_model
    
    shared.selected_embedding_model = selected_embedding

    return [gr.Dropdown(choices=data.models, value=selected), gr.Dropdown(choices=data.models, value=selected_embedding)]

(model_info, model_details, model_file, model_template, model_parameters) = ui.model_info.create_model_info()
ci = ui.chat_interface.create_chatinterface()
game = ui.game.create_game()
model_list = ui.dropdown_models.create_models(model_details, model_file, model_template, model_parameters)
embedding_model_list = ui.dropdown_models.create_models()

with gr.Blocks() as demo:
    gr.Markdown(value="# Llama in Chains")
    gr.TabbedInterface([ci, model_info, game], ["Chat", "Model details", "Game"])
    gr.TabbedInterface([model_list, embedding_model_list], ["Model", "Embedding Model"])
    demo.load(fn=load_data, outputs=[model_list, embedding_model_list])

if __name__ == "__main__":
    demo.launch(server_name=config.gradio_server_name, server_port=int(config.gradio_server_port),blocked_paths=config.blocked_paths)
