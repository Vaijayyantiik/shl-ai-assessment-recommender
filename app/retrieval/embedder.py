from sentence_transformers import SentenceTransformer

import json

import faiss

import numpy as np

import pickle


print("Loading embedding model...")


model = SentenceTransformer(

    "all-MiniLM-L6-v2"
)


print("Loading SHL catalog...")


with open(

    "data/shl_catalog.json",

    "r",

    encoding="utf-8"

) as f:

    catalog = json.load(f)


texts = []


for item in catalog:

    text = f"""

    Assessment Name:
    {item['name']}

    Description:
    {item.get('description', '')}

    Tags:
    {' '.join(item.get('tags', []))}

    URL:
    {item['url']}

    """

    texts.append(text)


print("Generating embeddings...")


embeddings = model.encode(texts)


dimension = len(embeddings[0])


print("Creating FAISS index...")


index = faiss.IndexFlatL2(dimension)


index.add(

    np.array(embeddings)
)


faiss.write_index(

    index,

    "vectorstore/shl.index"
)


with open(

    "vectorstore/catalog.pkl",

    "wb"

) as f:

    pickle.dump(

        catalog,

        f
    )


print("\nEmbeddings Created Successfully")