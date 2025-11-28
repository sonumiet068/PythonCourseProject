import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./chromadb_store")
collection = client.get_or_create_collection(name="bulk_test")

model = SentenceTransformer("all-MiniLM-L6-v2")

def batch(iterable,batch_size=500):
  l = len(iterable)
  for ndx in range(0,l,batch_size):
    yield iterable[ndx:ndx+batch_size]

documents = [f"This is a document {i}" for i in range(20000)]
ids = [str(i) for i in range(20000)]

for docs_batch,ids_batch in zip(batch(documents,1000),batch(ids,1000)):
  vectors = model.encode(docs_batch,batch_size=64)
  print(len(docs_batch))
  collection.add(
    ids = ids_batch,
    documents=docs_batch,
    embeddings = vectors
  )

results = collection.query(query_texts=["Notes docs"],n_results=10)
print(results)
print("Bulk Insert Done")





