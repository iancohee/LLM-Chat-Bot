import logging

from llama_index import ServiceContext, set_global_service_context
from local_llm import LocalLLM

class ChatBot:
    def __init__(self, llm: LocalLLM | None):
        self.llm = llm
        self.index = None
        self.service_context = None

        logging.debug(f"chat_bot; self.llm: {self.llm}")
        if self.llm is not None:
            logging.debug("setting service context")
            self.service_context = ServiceContext.from_defaults(
                llm="local", embed_model="local:BAAI/bge-small-en"
                )
            set_global_service_context(self.service_context)
    
    def set_index(self, index):
        self.index = index

    def query(self, query_str: str):
        return self.index.query(query_str)
