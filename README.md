LLM Chat Bot
===

## About
This is a basic chat bot written with [LLAMA Hub](https://llamahub.ai/) indexers.

Using indexers we can supplement prompts with contextual information without retraining the LLM.

The current supported Indexers are:
1. Wikipedia
1. Confluence (coming soon!)

## Usage
When using OpenAI API as the LLM backend, the environment variable {OPENAI_API_KEY} must be set to an application key generated at https://platform.openai.com/api-keys.

### Help Text
```
% python app.py
usage: app.py [-h] [--openai] -p PAGES --index {wikipedia,confluence} [--speech]
app.py: error: the following arguments are required: -p/--pages, --index
```

### Setup
Create environment and install dependencies

```
cd /path/to/clone
python3 -m venv .venv
pip install -r requirements.txt
```

### Example

```
OPENAI_API_KEY="..." python app.py --openai --pages="Gareth_Knight" --index wikipedia
```

Output:
```
[Enter query and press ENTER]

> Who was Gareth Knight?
>> Gareth Knight was a British occultist, ritual magician, author, and publisher. He had a deep interest in magic from an early age and became an initiate of the Society of the Inner Light, founded by the occultist Dion Fortune. Knight was actively involved in the Society for a decade, serving as its librarian and editor. He later co-founded the Helios Book Service, which aimed to publish and distribute occult-related books. Knight left the Society in 1965 and went on to publish numerous books on various occult subjects, including Christian esotericism, tarot reading, Arthurian legends, Celtic mythology, and the occult influence on J.R.R. Tolkien's works. He also founded his own esoteric order, known as the Gareth Knight Group, and hosted annual conventions at Greystone. Knight rejoined the Society of the Inner Light in 1998 and became Fortune's biographer, as well as compiling collections of her unpublished works. He passed away in 2022 at the age of 91. <<
>

```