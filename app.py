import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


# Loading environment variables from .env file
load_dotenv() 

# Function to chat with CSV data
def chat_with_csv(df,query):
    # Loading environment variables from .env file
    load_dotenv() 

    # Function to initialize conversation chain with GROQ language model
    #groq_api_key = os.environ['GROQ_API_KEY']

    # Initializing GROQ chat with provided API key, model name, and settings
    llm = ChatGroq(
    groq_api_key="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", model_name="llama3-70b-8192",
    temperature=0.6)
    # Initialize SmartDataframe with DataFrame and LLM configuration
    pandas_ai = SmartDataframe(df, config={"llm": llm})
    # Chat with the DataFrame using the provided query
    result = pandas_ai.chat(query)
    return result

# Set layout configuration for the Streamlit page
st.set_page_config(layout='wide')
# Set title for the Streamlit application
st.title("Tes Analisis by CSV")

# Upload multiple CSV files
input_csvs = st.sidebar.file_uploader("Upload CSV file", type=['csv'], accept_multiple_files=True)

# Check if CSV files are uploaded
if input_csvs:
    # Select a CSV file from the uploaded files using a dropdown menu
    selected_file = st.selectbox("Pilih  CSV file", [file.name for file in input_csvs])
    selected_index = [file.name for file in input_csvs].index(selected_file)

    #load and display the selected csv file 
    st.info("CSV Sukses di upload")
    data = pd.read_csv(input_csvs[selected_index])
    st.dataframe(data.head(5),use_container_width=True)

    #Enter the query for analysis
    st.info("Chat terkait CSV")
    input_text = st.text_area("Input query")

    #Perform analysis
    if input_text:
        if st.button("Chat dengan csv"):
            st.info("Pertanyaan: "+ input_text)
            result = chat_with_csv(data,input_text)
            st.success(result)




     
