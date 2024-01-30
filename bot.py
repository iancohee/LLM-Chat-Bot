from llama_index import ServiceContext, set_global_service_context
from local_llm import LocalLLM

class ChatBot:
    def __init__(self, llm: LocalLLM | None, index):
        self.llm = llm
        self.index = index

        if self.llm is not None:
            self.service_context = ServiceContext.from_defaults(
                llm=self.llm, embed_model="local:BAAI/bge-small-en"
                )
            set_global_service_context(self.service_context)
    
    def query(self, query_str):
        return self.index.query(query_str)
