from pathlib import Path
from llama_index import download_loader, VectorStoreIndex


__app_loader_name__ = 'PDFReader'

class PDFReaderIndex():
    def __init__(self, path: str):
        self.path = path
    
    def initialize(self):
        PDFReader = download_loader(__app_loader_name__)
        self.loader = PDFReader()
        self.documents = self.loader.load_data(file=Path(self.path))
        self.index = VectorStoreIndex.from_documents(self.documents)
        self.query_engine = self.index.as_query_engine()

    def query(self, query: str) -> str:
        return self.query_engine.query(query)