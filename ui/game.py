import gradio as gr
from config import config
import data
import ollama
import data.games
import shared
import re

game_instruction = None

def start_new_game():
    global game_instruction

    (game, prompt) = data.games.games_list[0]
    messages = [{"role": "user", "content": prompt}]
    response = ollama.chat(messages=messages, model=shared.selected_model, stream = False)
    response = response['message']['content']
    game_instruction = response
    return [response,
            0,
            # clean up chat history
            []
            ]


def take_action(prompt, history = None, model = None):
    global game_instruction

    (game, game_prompt) = data.games.games_list[0]

    messages = [{"role": "user", "content": game_prompt}, 
                {"role": "assistant", "content": game_instruction}] 
    if history:
        for u, a in history:
            messages.append({"role": "user", "content": u})
            messages.append({"role": "assistant", "content": a})
    messages.append({"role": "user", "content": prompt})

    partial_message = ''

    for chunk in ollama.chat(messages=messages, model=shared.selected_model, stream = True):
        new_token = (chunk['message']['content'])
        partial_message += new_token
        yield partial_message

def create_game():
    slider_progress = None

    textbox = gr.Textbox(elem_id="input_box", lines=3, min_width=800)
    chatbot = gr.Chatbot(show_copy_button=True, layout="panel")
    submit_btn = gr.Button(value="Submit")
    with gr.Blocks() as game:
        with gr.Row():
            with gr.Column():
                nem_game = gr.ClearButton(value='New Game', components = [chatbot])
                instruction = gr.Markdown(value='Click New Game to begin.')
                slider_progress = gr.Slider(label="Progress", value=0)
            with gr.Column():
                chat_interface = gr.ChatInterface(
                    fn=take_action,
                    textbox=textbox,
                    chatbot=chatbot,
                    submit_btn=submit_btn,
                    retry_btn=None,
                    undo_btn=None,
                    clear_btn=None,
                )
        nem_game.click(fn=start_new_game, outputs=[instruction, slider_progress, chat_interface.chatbot_state])
        @gr.on(triggers=[chatbot.change], inputs=[chatbot], outputs=[slider_progress])
        def update_slider(chatbot):
            progress = 0
            text = ""
            pattern = r"Progress:[\* ]*(\d+)"
            if len(chatbot) > 0:
                if len(chatbot[-1]) > 0:
                    if chatbot[-1][-1]:
                        text = chatbot[-1][-1]

            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                progress = int(match.group(1))
            return[progress]
    return game