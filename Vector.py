from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("D:\Projects\LLM\CSV_Chatbot\Car sales details\Car_sales.csv")

embeddings = OllamaEmbeddings(model = "mxbai-embed-large")

data_location = "./chrome_langchain_database"
document_add = not os.path.exists(data_location)

if document_add:
    documents =[]
    ids = []

    for i, row in df.iterrows():
        content = f"""
        Brand: {row['Brand']}
        Price: {row['Price']}
        Body: {row['Body']}
        Mileage: {row['Mileage']}
        EngineV: {row['EngineV']}
        Engine Type: {row['Engine Type']}
        Registration: {row['Registration']}
        Year: {row['Year']}
        Model: {row['Model']}
        """
        metadata = {
            "id": str(i),
            "Brand": row["Brand"],
            "Year": int(row["Year"]),
            "Engine Type": row["Engine Type"]
        }

        document = Document(
            page_content=content.strip(),
            metadata=metadata
        )

    ids.append(str(i))
    documents.append(document)


vector_store = Chroma(
    collection_name = "car_sales_data",
    persist_directory = data_location,
    embedding_function = embeddings
    

   


)

()
if document_add:
    vector_store.add_documents(documents)
    vector_store.persist()
retriever = vector_store.as_retriever(
    search_kwargs= {"k":5000}
)

query = "Show me gas cars after 2018"
docs = retriever.invoke(query)

# Manual filtering
filtered_docs = [
    doc for doc in docs
    if doc.metadata.get("Engine Type") == "Gas" and doc.metadata.get("Year", 0) > 2018
]