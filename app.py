import argparse
import logging
import pyttsx3
import sys

from args import *
from bot import ChatBot
from local_llm import LocalLLM, codellama_7b_instruct


def main(args: argparse.Namespace):
    llm = None
    if args.local == True:
        logging.info("OpenAI not enabled, initializing local LLM")
        llm = LocalLLM(model=codellama_7b_instruct)
        llm.initialize_llm(use_gpu=False);
    
    chat_bot = ChatBot(llm)
    index = get_index_from_args(args)
    chat_bot.set_index(index)

    speech_engine = None
    if args.speech == True:
        logging.info("initializing speech engine")
        speech_engine = pyttsx3.init()

    print("\n[Enter query and press ENTER]\n")
    while True:
        user_input = input("> ")
        response = chat_bot.query(user_input)
        print(f">> {response} <<")
        if speech_engine is not None:
            speech_engine.say(response)
            speech_engine.runAndWait()


if __name__ == '__main__':
    args = get_args()
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
    main(args)