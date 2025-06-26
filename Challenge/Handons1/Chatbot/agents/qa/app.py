from adk.agent import Agent
from adk.agent_server import AgentServer
from adk.devtools import start_dev_ui

import requests

class QAAgent(Agent):
    def name(self):
        return "QA Agent"
    
    def description(self):
        return "Orchestration for agents. And / or common questions"

    def handle(self, user_input, state, tools):
        # orchestrate the agents
        user_input_truncated = user_input.lower()


        # check if the user input is a question
        if not user_input.endswith("?"):
            return {"answer": "Vui lòng đặt câu hỏi với dấu hỏi ở cuối."}

        if "order" in user_input_truncated() or "đơn hàng" in user_input_truncated:
            res = requests.post("http://order_retrieval:8001/invoke", json={
                "input": user_input_truncated, 
                "conversation_id": state.get("conversation_id")})
            return {"answer": res.json()["answer"]}
        
        elif "product" in user_input_truncated or "sản phẩm" in user_input_truncated:
            res = requests.post("http://product_advisor:8002/invoke", json={"question": user_input})
            return {"answer": res.json()["answer"]}
        
        elif "bảo hành" in user_input_truncated or "đổi trả" in user_input:
            res = requests.post("http://frequent_qa:8003/invoke", json={"question": user_input})
            return {"answer": res.json()["answer"]}
        
        else:
            return {"answer": "Đây là agent QA. Câu hỏi của bạn sẽ được điều phối."}


if __name__ == "__main__":
    agent = QAAgent()
    server = AgentServer(agent)
    start_dev_ui(agent_server=server, host="0.0.0.0", port=8080)
