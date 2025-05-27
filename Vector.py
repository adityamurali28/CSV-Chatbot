from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv(r"D:\Projects\LLM\CSV_Chatbot\Car sales details\Car_sales.csv")

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
        Year: {row['Year']}
        Model: {row['Model']}
    """
    
    document = Document(
        page_content=content.strip(),
        metadata={"id": str(i)}
    )
    
    ids.append(str(i))
    documents.append(document)

vector_store = Chroma(
    collection_name = "car_sales_data",
    persist_directory = data_location,
    embedding_function = embeddings

)

if document_add:
    vector_store.document_add(documents=documents, ids=ids)
retriever = vector_store.as_retriever(
    search_kwargs= {"k":5000}
)