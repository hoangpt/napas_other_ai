
from adk.agent_server import AgentServer
from adk.agent import Agent, Message, AgentResponse, AgentMetadata

class NapasAgent(Agent):
    def __init__(self):
        super().__init__(
            name="napas-demo-agent",
            description="Napas chatbot demo, trả lời FAQ, lãnh đạo, sản phẩm."
        )

    def process_message(self, message: Message) -> AgentResponse:
        user = message.user
        content = message.content.lower()
        if "faq" in content:
            text = "Đây là các câu hỏi thường gặp của Napas: ..."
        elif "lãnh đạo" in content or "lanh dao" in content:
            text = "Đội ngũ lãnh đạo Napas gồm ..."
        elif "sản phẩm" in content or "product" in content:
            text = "Các sản phẩm chính của Napas gồm ..."
        else:
            text = f"Xin chào {user}, bạn vui lòng hỏi về FAQ, lãnh đạo, hoặc sản phẩm."
        return AgentResponse(
            content=text,
            metadata=AgentMetadata()
        )

if __name__ == "__main__":
    agent = NapasAgent()
    server = AgentServer(agent)
    server.run(port=8080)