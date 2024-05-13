import requests
import json
import gradio as gr

url = "http://localhost:11434/api/"


def generate_response(prompt, history, model):
    data = {"model": model, "stream": False, "prompt": prompt}

    response = requests.post(
        url + "generate",
        headers={"Content-Type": "application/json", "Connection": "close"},
        data=json.dumps(data),
    )

    if response.status_code == 200:
        bot_message = json.loads(response.text)["response"]
        history.append((prompt, bot_message))
        return bot_message
    else:
        print("Error: generate response:", response.status_code, response.text)


def generate_chat_response(prompt, history, model):
    messages = []
    for u, a in history:
        messages.append({"role": "user", "content": u})
        messages.append({"role": "assistant", "content": a})
    messages.append({"role": "user", "content": prompt})

    data = {"model": model, "stream": False, "messages": messages}

    response = requests.post(
        url + "chat",
        headers={"Content-Type": "application/json", "Connection": "close"},
        data=json.dumps(data),
    )

    if response.status_code == 200:
        bot_message = json.loads(response.text)["message"]["content"]
        return bot_message
    else:
        print("Error: generate response:", response.status_code, response.text)


def list_models():
    response = requests.get(
        url + "tags",
        headers={"Content-Type": "application/json", "Connection": "close"},
    )

    if response.status_code == 200:
        models = json.loads(response.text)["models"]
        return [d["model"] for d in models]
    else:
        print("Error:", response.status_code, response.text)


models = list_models()

prompts = [
    ("check grammar", """check grammar
---
"""),
    ("write a headline", """write a headline
---
"""),
    ("summarize", """summarize
---
"""),
    ("explain", """explain
---
"""),
    ("write unit test", """write unit test
---
"""),
]


def new_prompt_template(choice, tb):
    return gr.Textbox(value=choice, autofocus=True, autoscroll=True)


textbox = gr.Textbox(elem_id="input_box", lines=3, min_width=800)
chatbot = gr.Chatbot(show_copy_button=True, layout="panel")


with gr.Blocks() as chat_interface:
    with gr.Row():
        dropdown = gr.Dropdown(label="Model", choices=models)
        # select the first item as default model
        dropdown.value = "llama3:instruct"

        quick_prompt = gr.Radio(
            prompts, label="Quick Prompt", info="Overwrite input with a template"
        )
        quick_prompt.change(new_prompt_template, [quick_prompt, textbox], textbox)

    with gr.Column():
        chat = gr.ChatInterface(
            fn=generate_chat_response,
            additional_inputs=[dropdown],
            textbox=textbox,
            chatbot=chatbot,
        )

with gr.Blocks() as parameters:
    with gr.Row():
        gr.Dropdown(label="Model", choices=models)

demo = gr.TabbedInterface([chat_interface, parameters], ["Chat", "Parameters"])

if __name__ == "__main__":
    demo.launch()
