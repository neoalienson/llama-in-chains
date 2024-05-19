import gradio as gr
from config import config
import ui.chat_interface 
import ui.parameters
from config import config

demo = gr.TabbedInterface([ui.chat_interface.chat_interface, ui.parameters.parameters], ["Chat", "Parameters"])

if __name__ == "__main__":
    demo.launch(server_name=config.gradio_server_name)
