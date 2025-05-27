from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd
import numpy as np
from Vector import retriever
import streamlit as st

model = OllamaLLM(model ="llama3.2")
template = """
You are an expert who understood the car details in the car_sales.csv and answering questions





Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Streamlit UI
st.title("🚗 Car sales Q&A Bot")
st.markdown("Hi! Please ask your query on the car sales!")

# Input field
question = st.text_input("Your question:", "")

if question:
    with st.spinner("Thinking..."):
        Price = retriever.invoke(question)
        result = chain.invoke({"Price": Price, "question": question})
        st.markdown("### 🤖 Answer")
        st.write(result)
        st.markdown("### 📝 Relevant Price")
        st.write(Price)

