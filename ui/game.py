import gradio as gr
from config import config
import data
import ollama_lib
import data.games
import shared

game_instruction = None

def start_new_game():
    global game_instruction

    (game, prompt) = data.games.games_list[0]
    response = ollama_lib.generate_chat_response(prompt=prompt, model=shared.selected_model)
    game_instruction = response
    return gr.Markdown(value=response)


def take_action(prompt, history = None, model = None):
    global game_instruction

    (game, game_prompt) = data.games.games_list[0]

    starting = [(game_prompt, game_instruction)]
    if len(history) > 0:
        starting.extend(history)

    return ollama_lib.generate_chat_response(prompt, history=starting)

def create_game():
    textbox = gr.Textbox(elem_id="input_box", lines=3, min_width=800)
    chatbot = gr.Chatbot(show_copy_button=True, layout="panel")    
    with gr.Blocks() as game:
        with gr.Row():
            with gr.Column():
                nem_game = gr.Button(value='New Game')
                instruction = gr.Markdown()
                nem_game.click(fn=start_new_game, outputs=instruction)
            with gr.Column():
                gr.ChatInterface(
                    fn=take_action,
                    textbox=textbox,
                    chatbot=chatbot,
                    retry_btn=None,
                    undo_btn=None,
                    clear_btn=None,
                )

    return game