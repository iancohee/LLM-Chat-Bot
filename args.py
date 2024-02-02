import argparse
import logging

from pdf_index import PDFReaderIndex
from wikipedia_index import WikipediaIndex


__index_args = ['wikipedia', 'pdf', 'confluence']

def get_index_from_args(args: argparse.Namespace) -> WikipediaIndex | None:
    logging.debug(f"get_index_from")
    index = None
    if args.index not in __index_args:
        return index
    if args.index == 'wikipedia':
        index = WikipediaIndex()
        index.load_wiki_pages(list(args.pages.split(',')))
    elif args.index == 'pdf':
        index = PDFReaderIndex(args.file)
        index.initialize()
    elif args.index == 'confluence':
        print(f"confluence indexer is not implemented, yet!")
    return index

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--local", 
        help="Do not use OpenAI API, use a HuggingFace model locally. Requires --model option", 
        action='store_true')
    parser.add_argument(
        "-p", 
        "--pages", 
        help="Comma-separated list of page IDs to fetch for indexing with Wikipedia and Confluence. Example: \"Dublin,London,Casper%2C_Wyoming\"", 
        required=False)
    parser.add_argument(
        "--index", 
        help=f"Indexer to use for RAG. Supported indices: {__index_args}.", 
        choices=__index_args, 
        required=True)
    parser.add_argument(
        "-f", 
        "--file", 
        help="Path to file for PDF indexer", 
        required=False)
    parser.add_argument(
        "-m",
        "--model",
        help="Which model to use locally. Example: \"meta/codellama_7b_instruct\"",
        required=False)
    parser.add_argument(
        "--speech", 
        help="Use speech synthesis to read responses out loud.", 
        required=False, 
        action='store_true')
    return parser.parse_args()