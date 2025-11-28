import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.create_collection(name="bulk_test")

def batch(iterable, batch_size=500):
    l = len(iterable)
    for ndx in range(0, l, batch_size):
        yield iterable[ndx:ndx + batch_size]

documents = [f"This is document {i}" for i in range(20000)]
ids = [str(i) for i in range(20000)]

for docs_batch, ids_batch in zip(
    batch(documents, 500), 
    batch(ids, 500)
):
    collection.add(
        ids=ids_batch,
        documents=docs_batch
    )

print("Bulk insert with batches completed!")
