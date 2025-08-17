import streamlit as st
from src.langraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langraphagenticai.llms.groqllm import GroqLLM
from src.langraphagenticai.graph.graph_builder import GraphBuilder
from src.langraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langraph_agenticai_app():
    """
    Load the Langraph Agentic AI application using Streamlit UI.
    This function initializes the UI components and sets up the sidebar
    for user interactions.

    """

    #load UI
    ui= LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user input. Please check the configuration.")
        return
        
    user_message = st.chat_input("Enter your message here:")

    if user_message:
        try:
            #configure the llms
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_groq_llm()

            if not model:
                st.error("Failed to configure the LLM. Please check your API key and model selection.")
                return
            
            #initialize and set up the graph based on the selected use case
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("No use case selected. Please select a use case from the sidebar.")
                return
            
            #GraphBuilder class
            graph_builder = GraphBuilder(model)
            try:
                graph= graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error setting up graph: {e}")
                return

        except Exception as e:
            st.error(f"Error configuring LLM: {e}")
            return
    