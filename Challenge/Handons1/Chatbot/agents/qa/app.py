from google.adk.agents import Agent

class QAAgent(Agent):
    # The QAAgent class is a specialized agent designed to answer user questions or route them to the appropriate agent.
    # 
    # Attributes:
    #     name (str): The display name of the agent.
    #     model (str): The underlying model used for generating responses.
    #     description (str): A brief description of the agent's purpose.
    #     instruction (str): Instructions that guide the agent's behavior.
    #
    # Methods:
    #     __init__(): Initializes the QAAgent with predefined attributes and passes them to the base Agent class.
    def __init__(self):
        super().__init__(
            name="QA Agent",
            model="gemini-1.5-flash",  # or another supported model
            description="Orchestration for agents. And / or common questions",
            instruction="You are a helpful QA agent. Answer user questions or route them to the appropriate agent.",
        )

# Optionally, you can add a main block to run the agent with ADK's CLI or web UI
if __name__ == "__main__":
    agent = QAAgent()
    # To run with ADK CLI or web UI, use: adk run . or adk web from the terminal in this directory
