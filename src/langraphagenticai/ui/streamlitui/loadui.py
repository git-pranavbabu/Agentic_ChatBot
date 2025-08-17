import streamlit as st
import os

from src.langraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}
    
    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(),layout="wide")
        st.header(self.config.get_page_title())
        
        with st.sidebar:
            #get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            #llm selection
            self.user_controls['selected_llm'] = st.selectbox(
                "Select LLM",
                options=llm_options)
            
            if self.user_controls['selected_llm'] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls['selected_model'] = st.selectbox(
                    "Select Groq Model",
                    options=model_options)
                self.user_controls['GROQ_API_KEY'] = st.text_input(
                    "Enter Groq API Key",
                    type="password",
                    key="GROQ_API_KEY"
                )
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("Please enter your Groq API Key to use Groq models.")

            #usecase selection

            self.user_controls['selected_usecase'] = st.selectbox("Select Use Case",
                options=usecase_options)
        
        return self.user_controls
        # Add more UI components as needed
