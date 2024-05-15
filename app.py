import gradio as gr
from config import config
from chat_interface import chat_interface
from parameters import parameters
from config import config


demo = gr.TabbedInterface([chat_interface, parameters], ["Chat", "Parameters"])

if __name__ == "__main__":
    demo.launch()
