from langchain_community.document_loaders import CSVLoader
import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\Projects\LLM\local_excel_chatbot\Car sales details\Car_sales.csv")
df.head()

loader = CSVLoader(
    file_path="D:\Projects\LLM\local_excel_chatbot\Car sales details\Car_sales.csv",
    content_columns=["Brand", "Model", "Body", "Mileage","EngineV", "Engine Type", "Registration","Year", "Price"],
    csv_args={"delimiter": ","},
    autodetect_encoding=True
)

docs = loader.load()
