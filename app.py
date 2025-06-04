from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd
import numpy as np
from Vector import retriever
import streamlit as st
import os

model = OllamaLLM(model ="llama3.2")
template = """
You are a car sales data assistant. Use ONLY the context below to answer the question.

If the answer is not found in the context, reply with "I couldn't find that information in the uploaded car sales data."

### Context:
{context}

### Question:
{question}

### Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model



st.title("🚗 Car sales Q&A Bot")
st.markdown("Hi! Please ask your query on the car sales!")

question = st.text_input("Your question:", "")

if question:
    with st.spinner("Thinking..."):
        docs = retriever.invoke(question)
        context = "\n\n".join([doc.page_content for doc in docs])
        result = chain.invoke({"question": question, "context": context})
        st.markdown("### 🤖 Answer")
        st.write(result)
        st.markdown("### 📝 Relevant Records")
        st.write(context)




data_location = "./tmp_chroma_store"
if os.path.exists(data_location):
    shutil.rmtree(data_location)
