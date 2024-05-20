import requests
from config import config
import json
import shared

def model_details(model_name):
    data = {"name": model_name}

    response = requests.post(
        config.ollama_url + "show",
        headers={"Content-Type": "application/json", "Connection": "close"},
        data=json.dumps(data),
    )

    if response.status_code == 200:
        bot_message = json.loads(response.text)
        return bot_message
    else:
        print("Error: generate response:", response.status_code, response.text)

def generate_response(prompt, history, model = None):
    if model is None:
        model = shared.selected_model

    data = {"model": model, "stream": False, "prompt": prompt}

    response = requests.post(
        config.ollama_url + "generate",
        headers={"Content-Type": "application/json", "Connection": "close"},
        data=json.dumps(data),
    )

    if response.status_code == 200:
        bot_message = json.loads(response.text)["response"]
        history.append((prompt, bot_message))
        return bot_message
    else:
        print("Error: generate response:", response.status_code, response.text)


def generate_chat_response(prompt, history, model= None):
    if model is None:
        model = shared.selected_model

    messages = []
    for u, a in history:
        messages.append({"role": "user", "content": u})
        messages.append({"role": "assistant", "content": a})
    messages.append({"role": "user", "content": prompt})

    data = {"model": model, "stream": False, "messages": messages}

    response = requests.post(
        config.ollama_url + "chat",
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
        config.ollama_url + "tags",
        headers={"Content-Type": "application/json", "Connection": "close"},
    )

    if response.status_code == 200:
        models = json.loads(response.text)["models"]
        return [d["model"] for d in models]
    else:
        print("Error:", response.status_code, response.text)
