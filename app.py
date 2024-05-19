import gradio as gr
from config import config
import  ui.chat_interface 
import ui.parameters
from config import config
import ollama_lib
import data

def load_data():
    data.models = ollama_lib.list_models()
    return [
        gr.TextArea(value="No information"),
        gr.Dropdown(label="Model", choices=data.models, value="llama3:instruct"),
        gr.Dropdown(label="Model", choices=data.models, allow_custom_value=False)]

with gr.Blocks() as demo:
    gr.TabbedInterface([ui.chat_interface.chat_interface, ui.parameters.parameters], ["Chat", "Parameters"])
    demo.load(fn=load_data, inputs=None, outputs=[ui.parameters.pa_model_details, ui.parameters.pa_models, ui.chat_interface.ci_models])

if __name__ == "__main__":
    demo.launch(server_name=config.gradio_server_name, server_port=int(config.gradio_server_port),blocked_paths=config.blocked_paths)
