import torch
from llama_index.llms import HuggingFaceLLM
from llama_index.prompts import PromptTemplate

# Model names (make sure you have access on HF)
llama2_7B = "meta-llama/Llama-2-7b-hf"
llama2_7B_chat = "meta-llama/Llama-2-7b-chat-hf"
llama2_13B = "meta-llama/Llama-2-13b-hf"
llama2_13B_chat = "meta-llama/Llama-2-13b-chat-hf"
llama2_70B = "meta-llama/Llama-2-70b-hf"
llama2_70B_chat = "meta-llama/Llama-2-70b-chat-hf"
mixtral_8x7B_instruct = "mistralai/Mixtral-8x7B-Instruct-v0.1"
mistral_7b = "mistralai/Mistral-7B-v0.1"

default_llama2_model = llama2_13B_chat
default_system_prompt = """You are an AI assistant that answers questions in a friendly manner, based on the given source documents. Here are some rules you always follow:
- Generate human readable output, avoid creating output with gibberish text.
- Generate only the requested output, don't include any other language before or after the requested output.
- Never say thank you, that you are happy to help, that you are an AI agent, etc. Just answer directly.
- Generate professional language typically used in business documents in North America.
- Never generate offensive or foul language.
"""

class LocalLLM:
    def __init__(self, model=default_llama2_model, prompt=default_system_prompt):
        self.model = model
        self.prompt = PromptTemplate(
            "[INST]<<SYS>>\n" + prompt + "<</SYS>>\n\n{query_str}[/INST] "
            )
        self.llm = None
        
    def initialize_llm(self):
        self.llm = HuggingFaceLLM(
            context_window=4096,
            max_new_tokens=2048,
            generate_kwargs={"temperature": 0.0, "do_sample": False},
            query_wrapper_prompt=self.prompt,
            tokenizer_name=self.model,
            model_name=self.model,
            device_map="auto",
            # change these settings below depending on your GPU
            model_kwargs={"torch_dtype": torch.float16, "load_in_8bit": True},
            )
