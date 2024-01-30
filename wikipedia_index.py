from llama_index import download_loader, VectorStoreIndex


__app_loader_name__ = 'WikipediaReader'

class WikipediaIndex:
    def __init__(self):
        self.index = None
        WikipediaReader = download_loader(__app_loader_name__)
        self.loader = WikipediaReader()
        self.documents = None
        self.index = None

    def load_wiki_pages(self, wiki_pages: list):
        self.documents = self.loader.load_data(pages=wiki_pages)
        self.index = VectorStoreIndex.from_documents(self.documents)
        self.query_engine = self.index.as_query_engine()

    def query(self, query_str: str) -> str:
        return self.query_engine.query(query_str)
