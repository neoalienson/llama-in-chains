from chat_interface import chat_interface


with gr.Blocks() as parameters:
    with gr.Row():
        gr.Dropdown(label="Model")

demo = gr.TabbedInterface([chat_interface, parameters], ["Chat", "Parameters"])

if __name__ == "__main__":
    demo.launch()
