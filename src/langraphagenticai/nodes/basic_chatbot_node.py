from src.langraphagenticai.state.state import State

class BasicChatbotNode:
    """
    A simple chatbot node that can be used in a Langraph Agentic AI system.
    This node can handle basic chat interactions and is designed to be easily extendable.
    """

    def __init__(self, model):
        self.llm=model

    def process(self, state: State) -> dict:
        """
        Process the state and return a response based on the current state.
        
        Args:
            state (State): The current state of the chatbot interaction.
        
        Returns:
            dict: A dictionary containing the response from the chatbot.
        """
        try:
            # Generate a response using the LLM
            response = self.llm.invoke(state['messages'])
            return {"response": response}
        except Exception as e:
            return {"error": str(e)}
        

    