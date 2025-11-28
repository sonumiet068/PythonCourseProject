import chromadb
chroma = chromadb.Client()
collection = chroma.create_collection(name="my_vectors")
# collection.add(
#   ids=["1","2","3","4"],
#   documents=["This is a cat","This is a dog","This is a car","Beach is most beautiful place"]
# )
# total_results =collection.query(query_texts=["car"],n_results=8)
# print(f"Total details from vector db :{total_results}")
texts = [f"This is a document {i}" for i in range(100)]
ids = [str(i) for i in range(100)]
collection.add(
  ids =ids,documents=texts
)
results = collection.query(query_texts=["Car"],n_results=3)
print(results)
# results = collection.query(query_texts=["pet animal"],
#                  n_results=4)
# print(f"Detail on basis of query{results}")




