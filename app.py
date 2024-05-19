import gradio as gr
from config import config
import tabs.model_info
import tabs.chat_interface 
from config import config
import ollama_lib
import data
import ui

def load_data():
    data.models = ollama_lib.list_models()
    return [
        gr.Dropdown(label="Model", choices=data.models, value="llama3:instruct"),
        gr.Dropdown(label="Model", choices=data.models, allow_custom_value=False)]

with gr.Blocks() as demo:
    gr.TabbedInterface([tabs.chat_interface.chat_interface, tabs.model_info.parameters], ["Chat", "Model details"])
    demo.load(fn=load_data, inputs=None, outputs=[ui.mi_models, ui.ci_models])

if __name__ == "__main__":
    demo.launch(server_name=config.gradio_server_name, server_port=int(config.gradio_server_port),blocked_paths=config.blocked_paths)
