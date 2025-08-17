from langgraph.graph import StateGraph
from src.langraphagenticai.state.state import State
from langgraph.graph import START, END
from src.langraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:
    def __init__(self, model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_graph(self):
        """
        Builds a basic chatbot graph with a single node.
        """
        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        
        self.graph_builder.add_node("chatbot","self.basic_chatbot_node.process")
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self,usecase: str):
        """
        Sets up the graph based on the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        