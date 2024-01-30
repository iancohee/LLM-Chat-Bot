import argparse
import pyttsx3

from bot import ChatBot
from wikipedia_index import WikipediaIndex
from local_llm import LocalLLM, mistral_7b

index_args = ['wikipedia', 'confluence']


def get_index_from_args(args: argparse.Namespace) -> WikipediaIndex | None:
    index = None
    for i in index_args:
        if i == args.index:
            indexer = i
    if indexer == index_args[0]:
        index = WikipediaIndex()
        index.load_wiki_pages(list(args.pages.split(',')))
    elif args.index == index_args[1]:
        print(f"confluence indexer is not implemented, yet!")
    return index

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--openai", help="Use OpenAI API, must have OPENAI_API_KEY set", action='store_true')
    parser.add_argument("-p", "--pages", help="Comma-separated list of page IDs to fetch for indexing. Example: \"Dublin,London,Casper%2C_Wyoming\"", required=True)
    parser.add_argument("--index", help=f"Indexer to use for RAG. Supported indices: {index_args}. First match is used.", choices=index_args, required=True)
    parser.add_argument("--speech", help="Use speech synthesis to read responses out loud.", required=False, action='store_true')
    return parser.parse_args()

def main():
    args = get_args()
    index = get_index_from_args(args)

    llm = None
    if args.openai != True:
        print("[*] OpenAI not enabled, initializing local LLM")
        llm = LocalLLM(model=mistral_7b)
        llm.initialize_llm();
    chat_bot = ChatBot(llm, index)

    speech_engine = None
    if args.speech == True:
        print("[*] initializing speech engine")
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
    main()